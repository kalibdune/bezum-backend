from typing import Annotated

from fastapi import Depends, Request

from bezum.config import config
from bezum.db.schemas.user import UserSchema
from bezum.db.session import session_manager
from bezum.services.auth import AuthService
from bezum.utils.enums import TokenType

hash_len = config.app.hash_len


async def get_session():
    async with session_manager.session() as session:
        yield session


async def check_auth(request: Request, session=Depends(get_session)) -> UserSchema:
    access_token = request.cookies.get("access_token")
    return await AuthService(session).validate_token(access_token, TokenType.access)


async def res_check_auth(
    request: Request, session=Depends(get_session)
) -> UserSchema | None:
    try:
        return await check_auth(request, session)
    except:
        return None


OAuth = Annotated[UserSchema, Depends(check_auth)]
UnstrictedOAuth = Annotated[UserSchema | None, Depends(res_check_auth)]
