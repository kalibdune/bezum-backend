from uuid import UUID

from pydantic import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from bezum.db.schemas.purchase import PurchaseCreateSchema, PurchaseSchema, PurchaseUpdateSchema, PurchaseInDB
from bezum.db.schemas.user import UserSchema

from bezum.repositories.purchase import PurchaseRepository
from bezum.services.auth import AuthService
from bezum.utils.exceptions import AlreadyExistError, NotFoundError


class PurchaseService:
    def __init__(self, session: AsyncSession):
        self._session = session
        self._repository = PurchaseRepository(session)

    async def get_purchase_by_id(self, purchase_id: UUID) -> PurchaseSchema:
        purchase = await self._repository.get_by_id(purchase_id)
        if purchase is None:
            raise NotFoundError(f"purchase_id: {purchase_id}")
        return PurchaseSchema.model_validate(purchase, from_attributes=True)
    
    async def create_purchase(self, user: UserSchema, purchase: PurchaseCreateSchema) -> PurchaseSchema:
        purchase = PurchaseInDB(purchase.description, purchase.category, purchase.price, user.id)
        purchase = await self._repository.create(purchase.model_dump())
        return PurchaseSchema.model_validate(purchase, from_attributes=True)
    
    async def update_purchase_by_id(
        self, purchase_id: UUID, new_purchase: PurchaseUpdateSchema
    ) -> PurchaseSchema:
        purchase = await self.get_purchase_by_id(purchase_id)

        for key, value in new_purchase.model_dump(exclude_unset=True).items():
            setattr(purchase, key, value)
        
        purchase = await self._repository.update_by_id(purchase_id, purchase.model_dump())
        return PurchaseSchema.model_validate(purchase, from_attributes=True)
    
    async def delete_purchase_by_id(
            self, purchase_id: UUID
    ):
        purchase = await self.get_purchase_by_id(purchase_id)
        purchase = await self._repository.delete_by_id(purchase_id)
        # return ...