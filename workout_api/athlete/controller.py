## To create a router for athlete-related endpoints. Whatever that means. But  Iknow it created  a section in the API documnentation for  post athlete so it's a win!.
from datetime import datetime
from fastapi import APIRouter, status, Body, HTTPException
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate

from pydantic import UUID4
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
# from sqlalchemy.orm import joinedLoad
from uuid import uuid4

from workout_api.contrib.dependencies import DatabaseDependency, ParamsDependency
from workout_api.athlete.schemas import AthleteIn, AthleteOut, AthleteUpdate, AthleteQuery
from workout_api.athlete.models import AthleteModel
from workout_api.categories.models import CategoryModel
from workout_api.training_center.models import TrainingCenterModel


router = APIRouter()

@router.post(
	"/",
	tags=["athletes"],
	summary="Create a new athlete",
	status_code=status.HTTP_201_CREATED,
	response_model=AthleteOut
)
async def post(
	db_session: DatabaseDependency,
	athlete_in: AthleteIn = Body()
) -> AthleteOut:
	category = (
		await db_session.execute(select(CategoryModel).filter_by(name=athlete_in.category.name))
		).scalars().first()
	if not category:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail=f"Category not found for name: {athlete_in.category.name}"
		)


	training_center = (
		await db_session.execute(select(TrainingCenterModel).filter_by(name=athlete_in.training_center.name))
		).scalars().first()
	if not training_center:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail=f"Training Center not found for name: {athlete_in.training_center.name}"
		)
	
	try:
		athlete_out = AthleteOut(id=uuid4(), created_at=datetime.now(),**athlete_in.model_dump())
		athlete_model = AthleteModel(**athlete_out.model_dump(exclude={"category", "training_center"}), category_id=category.pk_id, training_center_id=training_center.pk_id)

		db_session.add(athlete_model)
		await db_session.commit()
	except IntegrityError:
		raise HTTPException(
			status_code=status.HTTP_303_SEE_OTHER,
			detail=f"Error creating athlete: There is already an athlete registered with cpf {athlete_in.cpf}"
		)
	except Exception as e:
		raise HTTPException(
			status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
			detail=f"Error creating athlete: {e}"
		)

	return athlete_out


@router.get(
	"/",
	summary="Query athletes",
	status_code=status.HTTP_200_OK,
	response_model=Page[AthleteQuery]
)
async def query(
	db_session: DatabaseDependency,
	params: ParamsDependency,
	name: str | None = None,
	cpf: str | None = None,
) -> Page[AthleteQuery]:
	query = select(AthleteModel)
	if name:
		query = query.filter(AthleteModel.name==name)
	if cpf:
		query = query.filter(AthleteModel.cpf==cpf)

	page = await paginate(db_session, query, params=params)

	total_pages = (page.total + params.size - 1) // params.size  # ceil division
	if params.page > total_pages and page.total > 0:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail=f"Page {params.page} does not exist. Total pages: {total_pages}."
		)
	elif not page.items:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail=f"No athletes found with given filters."
		)

	page.items = [
			AthleteQuery(
				name=athlete.name,
				category=athlete.category,
				training_center=athlete.training_center
			)
			for athlete in page.items
		]

	return page


@router.get(
	"/{id}",
	summary="Query an athlete by id",
	status_code=status.HTTP_200_OK,
	response_model=AthleteOut
)
async def query_id(id: UUID4, db_session: DatabaseDependency,) -> AthleteOut:
	athlete: AthleteOut = (
		await db_session.execute(select(AthleteModel).filter_by(id=id))
		).scalars().first()

	if not athlete:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail=f"Athlete not found for id: {id}"
		)

	return AthleteOut.model_validate(athlete)


@router.patch(
	"/{id}",
	summary="Update an athlete by id",
	status_code=status.HTTP_200_OK,
	response_model=AthleteOut
)
async def patch(id: UUID4, db_session: DatabaseDependency, athlete_up: AthleteUpdate = Body()) -> AthleteOut:
	athlete: AthleteOut = (
		await db_session.execute(select(AthleteModel).filter_by(id=id))
		).scalars().first()
	if not athlete:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail=f"Athlete not found for id: {id}"
		)
	athlete_up_dict = athlete_up.model_dump(exclude_unset=True)
	for key, value in athlete_up_dict.items():
		setattr(athlete, key, value)

	await db_session.commit()
	await db_session.refresh(athlete)
	return athlete


@router.delete(
	"/{id}",
	summary="Delete an athlete by id",
	status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(id: UUID4, db_session: DatabaseDependency,) -> None:
	athlete: AthleteOut = (
		await db_session.execute(select(AthleteModel).filter_by(id=id))
		).scalars().first()

	if not athlete:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail=f"Athlete not found for id: {id}"
		)

	await db_session.delete(athlete)
	await db_session.commit()

	return None