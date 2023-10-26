from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.cadastro import router as router_cadastro
from app.routes.contato import router as router_contato
from app.routes.permissao import router as router_permissao
from app.routes.razao import router as router_razao
from app.routes.notificacao import router as router_notificacao
from app.routes.feed import router as router_feed
from app.routes.form import router as router_form


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3306",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router=router_cadastro)
app.include_router(router=router_contato)
app.include_router(router=router_permissao)
app.include_router(router=router_razao)
app.include_router(router=router_notificacao)
app.include_router(router=router_feed)
app.include_router(router=router_form)