
from pydantic import BaseModel


class CurrencySchema(BaseModel):
    course: str
    value: float

