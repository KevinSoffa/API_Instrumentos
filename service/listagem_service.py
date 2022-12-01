from repository import listagem_repository


def listagem_service(listagem_dto: dict):

    response = listagem_repository(
        listagem_dto
    )

    return response or []
