from service import atualizar_service
from models.dto import AtualizarDTO
from .router import router
from fastapi import status


@router.patch('/{id}', status_code=status.HTTP_200_OK)
def atualizar_controller(id: str, atualizar_dto: AtualizarDTO):
    print("Entrou")
    return atualizar_service(
        id, 
        atualizar_dto
    )
