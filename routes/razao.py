from fastapi import APIRouter, status, HTTPException, Path, Query
from app.dao import dao_razao as daorazao
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.schemas import razao as schemas_razao

from fastapi import APIRouter

router = APIRouter(
    prefix="/razao",
    tags=["razao"]
)

@router.get('/get-reason/{user_id}')
def get_reason(user_id: int):

    login = daorazao.Getreason(user_id)
    if login:
        login_json = jsonable_encoder(login)
        return JSONResponse(status_code=status.HTTP_200_OK, content=login_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Erro to get"})

@router.post('/create-reason/')
def create_reason(reason: schemas_razao.Reason):

    login = daorazao.CreateReason(reason)
    if login:
        login_json = jsonable_encoder(login)
        return JSONResponse(status_code=status.HTTP_200_OK, content=login_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Erro to create"})

