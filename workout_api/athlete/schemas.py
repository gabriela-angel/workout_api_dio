## Schemas are used to define the structure of data for validation and serialization. Define the data you want to display
## BaseModel is the base class for creating Pydantic models
# Field is used to provide additional metadata and validation for model fields
from workout_api.contrib.schemas import BaseSchema, OutMixin
from workout_api.categories.schemas import CategoryIn
from workout_api.training_center.schemas import TrainingCenterAthlete
from pydantic import Field, PositiveFloat
from typing import Annotated, Optional

class Athlete(BaseSchema):
	# pk_id: int  -> not set by user
	# id: uuid -> not set by user

	# This "Annotated[type, return]" is from pydantic and is used to define the data types of each field
	name: Annotated[str, Field(description="Name of Athlete", examples=["Mark"], max_length=50)]
	cpf: Annotated[str, Field(description="CPF of Athlete", examples=["12345678901"], max_length=11)]
	age: Annotated[int, Field(description="Age of Athlete", examples=[22])]
	weight: Annotated[PositiveFloat, Field(description="Weight of Athlete in kg", examples=[59.6])]
	height: Annotated[PositiveFloat, Field(description="Height of Athlete in meters", examples=[1.65])]
	sex: Annotated[str, Field(description="Sex of Athlete [F/M]", examples=["F"], max_length=1)]
	category: Annotated[CategoryIn, Field(description="Category of Athlete")]
	training_center: Annotated[TrainingCenterAthlete, Field(description="Training Center of Athlete")]

# Schema for insertion
class AthleteIn(Athlete):
	pass

# The OutMixin is for the field "created_at" that is in the base schema
class AthleteOut(AthleteIn, OutMixin):
	pass

# Schema for updating
class AthleteUpdate(BaseSchema):
	name: Annotated[Optional[str], Field(None, description="Name of Athlete", examples=["Mark"], max_length=50)]
	age: Annotated[Optional[int], Field(None, description="Age of Athlete", examples=[22])]
	weight: Annotated[Optional[PositiveFloat], Field(None, description="Weight of Athlete in kg", examples=[59.6])]
	height: Annotated[Optional[PositiveFloat], Field(None, description="Height of Athlete in meters", examples=[1.65])]

# Schema for query returns
class AthleteQuery(BaseSchema):
	name: Annotated[Optional[str], Field(None, description="Name of Athlete", examples=["Mark"], max_length=50)]
	category: Annotated[CategoryIn, Field(description="Category of Athlete")]
	training_center: Annotated[TrainingCenterAthlete, Field(description="Training Center of Athlete")]
