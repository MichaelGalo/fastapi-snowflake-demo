from sqlmodel import SQLModel, Field


class SpaceWeather(SQLModel, table=True):
    __tablename__ = "STG_SPACE_WEATHER"
    messageID: str = Field(primary_key=True, index=True)
    messageType: str = Field()
    messageBody: str = Field()
    messageIssueTime_formatted: str = Field()
