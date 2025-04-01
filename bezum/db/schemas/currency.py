
from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    course: str
    value: str

