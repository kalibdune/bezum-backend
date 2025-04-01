import logging
from typing import Annotated

from fastapi import APIRouter, Depends, Request, Response, status
from fastapi.security import OAuth2PasswordRequestForm

from bezum.db.schemas.auth import RevokedTokensSchema
from bezum.endpoints.dependencies import OAuth, get_session
from bezum.services.auth import AuthService

router = APIRouter(prefix="/token")

logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    resp: Response,
    session=Depends(get_session),
):
    auth_service = AuthService(session)
    tokens = await auth_service.create_tokens(form_data.username, form_data.password)
    resp.set_cookie(
        "access_token", tokens.access_token, httponly=True, samesite="strict"
    )
