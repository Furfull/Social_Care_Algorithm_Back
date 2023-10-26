from fastapi import APIRouter, status, HTTPException, Path, Query
from app.dao import dao_contato as daocontato
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.schemas import contato as schemas_contato

from fastapi import APIRouter

router = APIRouter(
    prefix="/contato",
    tags=["contato"]
)

@router.post('/create-contact/')
def create_contact(contato_info: schemas_contato.Contact):

    contato = daocontato.Createcontact(contato_info)
    if contato:
        contato_json = jsonable_encoder(contato)
        return JSONResponse(status_code=status.HTTP_200_OK, content=contato_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Erro to create"})

@router.get('/show-contact/{user_id}')
def get_contact(user_id: int):

    login = daocontato.ShowContact(user_id)
    if login:
        login_json = jsonable_encoder(login)
        return JSONResponse(status_code=status.HTTP_200_OK, content=login_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Erro to get"})

@router.delete('/delete-contact/{iuser_idd}')
def delete_contact(user_id: int):

    login = daocontato.DeleteContact(user_id)
    if login:
        login_json = jsonable_encoder(login)
        return JSONResponse(status_code=status.HTTP_200_OK, content=login_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Erro to delete"})

