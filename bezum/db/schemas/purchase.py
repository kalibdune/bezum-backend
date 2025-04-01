from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr


class PurchaseBaseSchema(BaseModel):
    description: str
    category: str
    price: float


class PurchaseSchema(PurchaseBaseSchema):
    id: UUID
    created_at: datetime
    updated_at: datetime
    user_id: UUID


class PurchaseCreateSchema(PurchaseBaseSchema):
    ...


class PurchaseUpdateSchema(BaseModel):
    description: str | None = None
    category: str | None = None
    price: float | None = None


class PurchaseInDB(PurchaseBaseSchema):
    user_id: UUID