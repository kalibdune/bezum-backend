from sqlalchemy import select
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from bezum.db.models.purchase import Purchase
from bezum.repositories.base import SQLAlchemyRepository


class PurchaseRepository(SQLAlchemyRepository):
    model = Purchase

    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
    
    async def get_all_by_user_id(self, user_id: UUID) -> list[Purchase] | None:
        stmt = select(self.model).where(self.model.user_id == user_id)
        return await self._session.scalars(stmt)