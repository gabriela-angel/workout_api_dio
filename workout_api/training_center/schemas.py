from workout_api.contrib.schemas import BaseSchema
from pydantic import Field, UUID4
from typing import Annotated

class TrainingCenterIn(BaseSchema):
	name: Annotated[str, Field(description="Name of Training Center", examples=["Ironfist"], max_length=20)]
	address: Annotated[str, Field(description="Address of Training Center", examples=["123 Main St"], max_length=60)]
	owner: Annotated[str, Field(description="Owner of Training Center", examples=["John Doe"], max_length=30)]

class TrainingCenterOut(TrainingCenterIn):
	id: Annotated[UUID4, Field(description="ID of Training Center", examples=[1])]

class TrainingCenterAthlete(BaseSchema):
	name: Annotated[str, Field(description="Name of Training Center", examples=["Ironfist"], max_length=20)]