from fastapi import APIRouter
from decouple import config


router = APIRouter(
    prefix=config('PREFIXO'),
    tags=[],
)