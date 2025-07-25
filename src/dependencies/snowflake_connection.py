import os
from dotenv import load_dotenv
import snowflake.connector
from src.dependencies.logger_init import setup_logging

load_dotenv()
logger = setup_logging()


def get_snowflake_connection():
    account = os.getenv("SNOWFLAKE_ACCOUNT")
    user = os.getenv("SNOWFLAKE_USER")
    password = os.getenv("SNOWFLAKE_PASSWORD")
    database = os.getenv("SNOWFLAKE_DATABASE")
    warehouse = os.getenv("SNOWFLAKE_WAREHOUSE")
    role = os.getenv("SNOWFLAKE_ROLE")
    schema = os.getenv("SNOWFLAKE_SCHEMA_SILVER")

    logger.info(
        f"Connecting to Snowflake: account={account}, user={user}, database={database}, schema={schema}, warehouse={warehouse}, role={role}"
    )
    try:
        snowflake_connection = snowflake.connector.connect(
            user=user,
            password=password,
            account=account,
            database=database,
            schema=schema,
            warehouse=warehouse,
            role=role,
        )
        logger.info("Snowflake connection established successfully.")
        return snowflake_connection
    except Exception as e:
        logger.error(f"Failed to connect to Snowflake: {e}")
        raise


def test_snowflake_connection():
    try:
        logger.info("Testing Snowflake connection with SELECT CURRENT_VERSION().")
        conn = get_snowflake_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT CURRENT_VERSION()")
        result = cursor.fetchone()
        logger.info(f"Snowflake connection successful. Version: {result[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        logger.error(f"Snowflake connection failed: {e}")
