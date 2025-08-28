from workout_api.contrib.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer

class CategoryModel(BaseModel):
	__tablename__ = "categories"

# The id in the base model is the UUID, and that is used so we don't expose the private key to the user
	pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
	name: Mapped[str] = mapped_column(String(10), nullable=False, unique=True)
	athletes: Mapped[list["AthleteModel"]] = relationship(back_populates="category")