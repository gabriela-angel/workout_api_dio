from typing import Annotated
from workout_api.config.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from fastapi_pagination import Params

DatabaseDependency = Annotated[AsyncSession, Depends(get_session)]
ParamsDependency = Annotated[Params, Depends(Params)]