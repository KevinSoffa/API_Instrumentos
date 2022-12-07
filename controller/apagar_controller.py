from service import apagar_service
from .router import router
from fastapi import status


@router.delete('/{id}', status_code=status.HTTP_200_OK)
def apagar_controller(id: str):
    return apagar_service(id)
