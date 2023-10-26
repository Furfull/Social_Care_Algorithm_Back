from fastapi import APIRouter, status, HTTPException, Path, Query
from app.dao import dao_notificacao as daonotificacao
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.schemas import notificacao as schemas_notificacao

from fastapi import APIRouter

router = APIRouter(
    prefix="/notificacao",
    tags=["notificacao"]
)

@router.get('/get-notification/{user_id}')
def get_notification(user_id: int):

    login = daonotificacao.Getnotification(user_id)
    if login:
        login_json = jsonable_encoder(login)
        return JSONResponse(status_code=status.HTTP_200_OK, content=login_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Erro to get"})

@router.post('/create-notification/')
def create_notification(notification: schemas_notificacao.Notification):

    login = daonotificacao.CreateNotification(notification)
    if login:
        login_json = jsonable_encoder(login)
        return JSONResponse(status_code=status.HTTP_200_OK, content=login_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Erro to create"})

