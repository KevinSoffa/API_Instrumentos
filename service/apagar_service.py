from repository import apagar_repository
from fastapi import HTTPException
from bson import ObjectId


def apagar_service(id: ObjectId):
    response = apagar_repository(id)

    if response is None:
        return HTTPException(
            500,
            detail='id não encontrado!'
        )

    if response:
        return HTTPException(
            200,
            detail='Objeto excluído com SUCESSO!'
        )

    raise HTTPException(404)
