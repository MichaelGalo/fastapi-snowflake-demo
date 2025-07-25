from sqlmodel import SQLModel, Field


class SpaceWeather(SQLModel, table=True):
    messageID: str = Field(primary_key=True, index=True)
    messageType: str = Field()
    messageBody: str = Field()
    messageIssueTime: str = Field()
