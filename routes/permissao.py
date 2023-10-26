from fastapi import APIRouter, status, HTTPException, Path, Query
from app.dao import dao_permissao as daopermissao
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.schemas import permissao as schemas_permissao

from fastapi import APIRouter

router = APIRouter(
    prefix="/permissao",
    tags=["permissao"]
)

@router.get('/facebook-permission/{user_id}')
def get_facebook_permission(user_id: int):

    login = daopermissao.PermissionFacebookState(user_id)
    if login:
        login_json = jsonable_encoder(login)
        return JSONResponse(status_code=status.HTTP_200_OK, content=login_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Erro to get"})

@router.put('/update-facebook-permission/{user_id}-{state}')
def update_facebook_permission(user_id: int, state: int):

    login = daopermissao.UpdatePermission(user_id, state)
    if login:
        login_json = jsonable_encoder(login)
        return JSONResponse(status_code=status.HTTP_200_OK, content=login_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Erro to update"})

