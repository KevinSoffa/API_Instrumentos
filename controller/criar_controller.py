from service import criarservice
from models.dto import CriarDTO
from .router import router
from fastapi import status


@router.post('', status_code=status.HTTP_201_CREATED)
def criar_controller(dto: CriarDTO):
    return criarservice(dto)
