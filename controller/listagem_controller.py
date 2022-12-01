from models.dto.listagem_dto import ListagemDTO
from service import listagem_service
from fastapi import status, Depends
from .router import router


@router.get('', status_code=status.HTTP_200_OK)
def listagem_controller(
    listagem_dto: ListagemDTO = Depends()
):

    return listagem_service(
        listagem_dto.__dict__,
    )
