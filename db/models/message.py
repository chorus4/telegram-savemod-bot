from sqlmodel import SQLModel, Field


class Message(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    chat_id: int
    content: str
    type: str
    from_username: str