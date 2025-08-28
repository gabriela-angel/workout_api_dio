##  This file is for internal use by asyncio. It is used to ?
from fastapi import APIRouter
from workout_api.athlete.controller import router as athlete_router
from workout_api.categories.controller import router as category_router
from workout_api.training_center.controller import router as training_center_router

api_router = APIRouter()
api_router.include_router(athlete_router, prefix="/athletes", tags=["athletes"])
api_router.include_router(category_router, prefix="/categories", tags=["categories"])
api_router.include_router(training_center_router, prefix="/training_centers", tags=["training_centers"])