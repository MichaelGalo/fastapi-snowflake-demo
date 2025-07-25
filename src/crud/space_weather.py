from sqlalchemy import select
from sqlalchemy.orm import Session
from src.models.space_weather import SpaceWeather
from src.dependencies.sqlalchemy_connection import sqlalchemy_engine


def fetch_space_weather():
    engine = sqlalchemy_engine()
    with Session(engine) as session:
        stmt = select(SpaceWeather)
        results = session.execute(stmt).scalars().all()
        # Convert model instances to dicts for FastAPI serialization
        space_weather_list = [weather.model_dump() for weather in results]
    return space_weather_list
