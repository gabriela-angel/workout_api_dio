# WorkoutAPI

WorkoutAPI is a FastAPI-based RESTful API for managing athletes, training centers, and categories in a workout or sports context. It uses PostgreSQL as the database and SQLAlchemy for ORM, with Alembic for migrations.

## Features

- Manage athletes, training centers, and categories
- CRUD operations for all entities
- Pagination support for listing endpoints
- Asynchronous database access with SQLAlchemy and asyncpg
- Alembic migrations for database schema management

## Project Structure

```
workout_api/
├── main.py                # FastAPI app entry point
├── routers.py             # API router setup
├── athlete/               # Athlete domain (models, schemas, controller)
├── categories/            # Category domain (models, schemas, controller)
├── training_center/       # Training center domain (models, schemas, controller)
├── config/                # Configuration (database, settings)
├── contrib/               # Shared dependencies, base models, schemas, repository
```

## Getting Started

### Prerequisites

- Python 3.12
- Docker (for running PostgreSQL)
- [Pipenv](https://pipenv.pypa.io/en/latest/) (recommended)

### Setup

1. **Clone the repository**

   ```sh
   git clone <repo-url>
   cd workout-api
   ```

2. **Set up environment variables**

   Copy the example environment file and fill in your own values:
   ```sh
   cp .env.example .env
   ```
   Then edit `.env` and set your database credentials as needed:
   ```
   POSTGRES_USER=youruser
   POSTGRES_PASSWORD=yourpassword
   POSTGRES_DB=workout_db
   DB_USER=youruser
   DB_PASSWORD=yourpassword
   DB_HOST=localhost
   DB_NAME=workout_db
   ```

3. **Start PostgreSQL with Docker Compose**

   ```sh
   docker-compose up -d
   ```

4. **Install dependencies**

   ```sh
   pipenv install
   pipenv shell
   ```

5. **Run database migrations**

   ```sh
   make run-migrations
   ```

6. **Start the FastAPI server**

   ```sh
   make run
   ```

7. **Access the API docs**

   Open [http://localhost:8000/docs](http://localhost:8000/docs) in your browser.

## Database Migrations

- **Create a new migration:**
  ```sh
  make create-migrations m="your migration message"
  ```
- **Apply migrations:**
  ```sh
  make run-migrations
  ```

## Configuration

- Database settings are in `workout_api/config/settings.py` and can be overridden with environment variables.
- Alembic configuration is in `alembic.ini`.

## API Endpoints

- `/athletes` - Manage athletes
- `/categories` - Manage categories
- `/training_centers` - Manage training centers

See the interactive docs at `/docs` for details.

## License