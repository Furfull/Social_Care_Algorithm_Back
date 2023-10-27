from fastapi import APIRouter, status, HTTPException, Path, Query
from app.dao import dao_feed as daofeed
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.schemas import feed as schemas_feed
from app.services.persist_feed import persist_data

from fastapi import APIRouter

router = APIRouter(
    prefix="/feed",
    tags=["feed"]
)

@router.get('/get-all-feed/')
def get_all_feed():

    login = daofeed.GetAllFeed()
    if login:
        login_json = jsonable_encoder(login)
        return JSONResponse(status_code=status.HTTP_200_OK, content=login_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Erro to get"})


@router.get('/get-feed-by-user-id/{user_id}')
def get_feed_by_user_id(user_id: int):

    login = daofeed.GetFeedByUserId(user_id)
    if login:
        login_json = jsonable_encoder(login)
        return JSONResponse(status_code=status.HTTP_200_OK, content=login_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Erro to get"})

@router.get('/get-feed-by-rate/{column}-{item}')
def get_feed_by_rate(column: str, item: str):

    login = daofeed.GetFeedByRate(column, item)
    if login:
        login_json = jsonable_encoder(login)
        return JSONResponse(status_code=status.HTTP_200_OK, content=login_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Erro to get"})


@router.post('/create-feed/')
def create_feed(feed: schemas_feed.Feed):

    login = daofeed.CreateFeed(feed)
    if login:
        login_json = jsonable_encoder(login)
        return JSONResponse(status_code=status.HTTP_200_OK, content=login_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Erro to create"})

@router.get('/analyse-facebook/')
def persist_data_in():

    login = persist_data()
    if login:
        login_json = jsonable_encoder(login)
        return JSONResponse(status_code=status.HTTP_200_OK, content=login_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Erro to create"})
