from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .config import settings
from .routes  import cart_router, product_router, categories_router
from .database import init_db

app = FastAPI(
    title=settings.app_name,
    debug = settings.debug,
    docs_url='/api/docs',
    redoc_url='/api/redoc',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = settings.cors_origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.mount('/static', StaticFiles(directory=settings.static_dir), name = 'static')

app.include_router(product_router)
app.include_router(categories_router)
app.include_router(cart_router)

@app.on_event('startup')
def on_startup():
    init_db()

@app.get('/')
def root():
    return {
        "message":"Welcome to project",
        'docs':"api/docs",
    }

@app.get('/health')
def health_check():
    return {'status':'healthy'}
