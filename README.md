# fastapi-snowflake-demo

This project is a FastAPI demo application that connects to a Snowflake database and exposes data via a REST API.

## Features

- FastAPI backend for serving data from Snowflake
- Secure connection using environment variables (.env)
- Logging for API and database operations
- Modular code structure for CRUD operations and models
- Example endpoint: `/space_weather` returns data from the `STG_SPACE_WEATHER` table

## Project Structure

- `src/` — Source code
  - `main.py` — FastAPI app entry point
  - `crud/` — CRUD operations (e.g., `space_weather.py`)
  - `models/` — Pydantic/SQLModel models (e.g., `space_weather.py`)
  - `dependencies/` — Database connection and logging setup
- `tests/` — Unit tests
- `logs/` — Log files

## Setup

1. Clone the repository
2. Create and activate a Python virtual environment
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Add your Snowflake credentials to a `.env` file in the project root
5. Run the app:
   ```bash
   uvicorn src.main:app --reload
   ```

## Usage

- Visit `http://localhost:8000/docs` for interactive API documentation
- Example endpoint:
  - `GET /space_weather` — Returns space weather data from Snowflake