from repository import listagem_repository
from fastapi import HTTPException


def listagem_service(listagem_dto: dict):

    response = listagem_repository(
        listagem_dto
    )

    if response:
        return response or []

    raise HTTPException(400)
