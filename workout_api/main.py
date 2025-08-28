from fastapi import FastAPI
from workout_api.routers import api_router
from fastapi_pagination import add_pagination

# Create FastAPI instance with a title
app = FastAPI(title="WorkoutAPI")
app.include_router(api_router)
add_pagination(app)

# Since we have put the command on the Makefile, we I have commented this out. If we wanted it to run when we so $python main.py, then we would need it.

# if __name__ == "__main__":
#     import uvicorn
    # Run the application with Uvicorn, this is our local server
    # The reload=True option is useful during development to auto-reload on code changes
    # Log level is set to "info" for more detailed logging
    # uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)