from workout_api.contrib.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, DateTime, ForeignKey
from datetime import datetime

class AthleteModel(BaseModel):
	__tablename__ = "athletes"

# The id in the base model is the UUID, and that is used so we don't expose the private key to the user
	pk_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
	name: Mapped[str] = mapped_column(String(50), nullable=False)
	cpf: Mapped[str] = mapped_column(String(11), nullable=False, unique=True)
	age: Mapped[int] = mapped_column(Integer, nullable=False)
	weight: Mapped[float] = mapped_column(Float, nullable=False)
	height: Mapped[float] = mapped_column(Float, nullable=False)
	sex: Mapped[str] = mapped_column(String(1), nullable=False)
	created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, nullable=False)
	# Relstionships, back_populates is used to define the relationship between two tables
	category: Mapped["CategoryModel"] = relationship(back_populates="athletes", lazy="selectin")
	category_id: Mapped[int] = mapped_column(ForeignKey("categories.pk_id"), nullable=False)
	training_center: Mapped["TrainingCenterModel"] = relationship(back_populates="athletes", lazy="selectin")
	training_center_id: Mapped[int] = mapped_column(ForeignKey("training_centers.pk_id"), nullable=False)