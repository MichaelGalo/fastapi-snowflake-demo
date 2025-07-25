from src.dependencies.snowflake_connection import get_snowflake_connection


def fetch_space_weather():
    conn = get_snowflake_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            'SELECT "messageID", "messageType", "messageBody", "messageIssueTime_formatted" FROM STG_SPACE_WEATHER'
        )
        rows = cursor.fetchall()
        space_weather_list = []

        for row in rows:
            space_weather_list.append(row)

        cursor.close()
        return space_weather_list

    finally:
        conn.close()
