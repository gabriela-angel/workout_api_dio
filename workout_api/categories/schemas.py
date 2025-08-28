from workout_api.contrib.schemas import BaseSchema
from pydantic import Field, UUID4
from typing import Annotated

class CategoryIn(BaseSchema):
	name: Annotated[str, Field(description="Name of Category", examples=["Dance"], max_length=10)]

class CategoryOut(CategoryIn):
	id: Annotated[UUID4, Field(description="ID of Category", examples=[1])]
