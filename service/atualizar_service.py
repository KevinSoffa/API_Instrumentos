from repository import atualizar_repository
from models.dto import AtualizarDTO
from fastapi import HTTPException


def atualizar_service(id: str, atualizar_dto: AtualizarDTO):
    dados = atualizar_dto.__dict__

    response = atualizar_repository(
        id,
        dados,
    )
    print(response)

    if response is None:
        return HTTPException(500)

    if response:
        return response

    raise HTTPException(404)
