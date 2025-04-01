from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from bezum.db.models.base import Base, TimeStampMixin

if TYPE_CHECKING:
    from bezum.db.models.user import User


class Purchase(Base, TimeStampMixin):
    __tablename__ = "purchase"

    description: Mapped[str] = mapped_column(nullable=True)
    category: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    user_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("usr.id"))

    user: Mapped["User"] = relationship(
        "User",
        back_populates="purchases"
    )

    def __repr__(self) -> str:
        attrs = ", ".join(
            f"{key}={value!r}"
            for key, value in self.__dict__.items()
            if not key.startswith("_")
        )
        return f"Purchase({attrs})"

    class Config:
        orm_mode = True
