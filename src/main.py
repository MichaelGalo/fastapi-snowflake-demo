from fastapi import FastAPI

from src.crud.space_weather import fetch_space_weather
from src.dependencies.logger_init import setup_logging

logger = setup_logging()

app = FastAPI()


@app.get("/")
async def read_root():
    logger.info("Root endpoint accessed.")
    return {
        "message": "Welcome to the FastAPI demo! Visit /docs for API documentation and how to use this."
    }


@app.get("/space_weather")
async def read_space_weather():
    logger.info("/space_weather endpoint accessed.")
    try:
        data = fetch_space_weather()
        logger.info(f"Fetched {len(data)} records from STG_SPACE_WEATHER.")
        return {"data": data}
    except Exception as e:
        logger.error(f"Error fetching space weather data: {e}")
        return {"error": str(e)}
