import logging
from uuid import UUID

from fastapi import APIRouter, Depends, Response, status

from bezum.db.schemas.purchase import PurchaseCreateSchema, PurchaseSchema, PurchaseUpdateSchema
from bezum.endpoints.dependencies import OAuth, get_session
from bezum.services.purchase import PurchaseService

router = APIRouter(prefix="/purchase")
hash_router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/", response_model=PurchaseSchema, status_code=status.HTTP_201_CREATED)
async def create_purchase(
    data: PurchaseCreateSchema, user: OAuth, session=Depends(get_session)
):
    purchase_service = PurchaseService(session)
    return await purchase_service.create_purchase(user, data)


@router.get("/{id}/", response_model=PurchaseSchema, status_code=status.HTTP_200_OK)
async def get_purchase_by_id(auth: OAuth, id: UUID, session=Depends(get_session)):
    purchase_service = PurchaseService(session)
    return await purchase_service.get_purchase_by_id(id)


@router.patch("/{id}/", response_model=PurchaseSchema, status_code=status.HTTP_200_OK)
async def update_purchase(
    data: PurchaseUpdateSchema, auth: OAuth, id: UUID, session=Depends(get_session)
):
    purchase_service = PurchaseService(session)
    return await purchase_service.update_purchase_by_id(id, data)


@router.delete("/{id}/", response_model=PurchaseSchema, status_code=status.HTTP_200_OK)
async def delete_purchase(auth: OAuth, id: UUID, session=Depends(get_session)):
    purchase_service = PurchaseService(session)
    return await purchase_service.delete_purchase_by_id(id)
