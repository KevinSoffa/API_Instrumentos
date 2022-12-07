from repository import atualizar_repository
from models.dto import AtualizarDTO
from fastapi import HTTPException
from bson import ObjectId


def atualizar_service(id: ObjectId, atualizar_dto: AtualizarDTO):
    dados = atualizar_dto.__dict__

    response = atualizar_repository(
        id,
        dados,
    )

    if response is None:
        return HTTPException(500)

    if response:
        return response

    raise HTTPException(404)
