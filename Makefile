# -----    VARIABLES -----
# PYTHON=python3
# -----    RULES     -----

run:
	@echo "Starting the FastAPI server..."
	@uvicorn workout_api.main:app --reload

create-migrations:
	@echo "Creating a new Alembic migration..."
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m "$(m)"
# m is the message for the migration

run-migrations:
	@echo "Running Alembic migrations..."
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head