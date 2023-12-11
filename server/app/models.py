from pydantic import BaseModel


class UserInput(BaseModel):
    app_type: str
    performance: bool
