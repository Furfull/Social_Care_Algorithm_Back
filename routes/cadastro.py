from fastapi import APIRouter, status, HTTPException, Path, Query
from app.dao import dao_cadastro as daocadastro
from app.dao import dao_permissao as daopermissao
from app.dao import dao_form as daoform
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.schemas import cadastro as schemas_cadastro

from fastapi import APIRouter

router = APIRouter(
    prefix="/cadastro",
    tags=["cadastro"]
)

@router.post('/create-user/')
def create_user(cadastro_info: schemas_cadastro.User):

    cadastro = daocadastro.CreateUser(cadastro_info)
    daopermissao.CreatePermission()
    daoform.CreateForm()
    if cadastro:
        cadastro_json = jsonable_encoder(cadastro)
        return JSONResponse(status_code=status.HTTP_200_OK, content=cadastro_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Erro to create"})

@router.get('/login-user/{user}-{password}')
def login_user(user: str, password: str):

    login = daocadastro.LoginUser(user, password)
    if login:
        login_json = jsonable_encoder(login)
        return JSONResponse(status_code=status.HTTP_200_OK, content=login_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Erro to login"})

