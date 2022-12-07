from service import detalhe_service
from bson import ObjectId
from fastapi import status
from .router import router


@router.get('/{id}', status_code=status.HTTP_200_OK)
def detalhe_controller(id: str):
    return detalhe_service(id)
