from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import UUID
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from uuid import uuid4

# Here we will put a standard field that will be in all tables
class BaseModel(DeclarativeBase):
	# From sqlalchemy, we can use Mapped to define the type of the field
	# and mapped_column to define the column properties
	# nullable=False means that this field cannot be null
	# unique=True means that this field must be unique in the table
	# primary_key=True means that this field is the primary key of the table
	# default=uuid4 means that the default value of this field will be a new UUID
	id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), default=uuid4, unique=True, nullable=False)