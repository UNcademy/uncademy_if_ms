from distutils.command.config import config
import imp

from fastapi import FastAPI
import models.model
from routes.routes import router
from config.config import engine

models.model.InvoiceDetail.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/book", tags=["book"])