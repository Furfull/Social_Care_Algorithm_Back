from fastapi import APIRouter, status, HTTPException, Path, Query
from app.dao import dao_form as daoform
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.schemas import form as schemas_form

from fastapi import APIRouter

router = APIRouter(
    prefix="/form",
    tags=["form"]
)

@router.get('/get-all-form/')
def get_all_form():

    login = daoform.GetAllForm()
    if login:
        login_json = jsonable_encoder(login)
        return JSONResponse(status_code=status.HTTP_200_OK, content=login_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Erro to get"})

@router.get('/get-form-by-user-id/{user_id}')
def get_form_by_user_id(user_id: int):

    login = daoform.GetFormByUserId(user_id)
    if login:
        login_json = jsonable_encoder(login)
        return JSONResponse(status_code=status.HTTP_200_OK, content=login_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Erro to get"})

@router.get('/get-form-by-rate/{column}-{item}')
def get_form_by_rate(column: str, item: str):

    login = daoform.GetFormByRate(column, item)
    if login:
        login_json = jsonable_encoder(login)
        return JSONResponse(status_code=status.HTTP_200_OK, content=login_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Erro to get"})


@router.post('/create-form/')
def create_form(form: schemas_form.Form):

    login = daoform.CreateForm(form)
    if login:
        login_json = jsonable_encoder(login)
        return JSONResponse(status_code=status.HTTP_200_OK, content=login_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Erro to update"})

@router.put('/update-form/{user_id}')
def uptade_form(form: schemas_form.Form, user_id: int):

    login = daoform.UpdateFormByUserId(form, user_id)
    if login:
        login_json = jsonable_encoder(login)
        return JSONResponse(status_code=status.HTTP_200_OK, content=login_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Erro to create"})

