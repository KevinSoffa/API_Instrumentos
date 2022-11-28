from repository import criar_repository
from models.dto import CriarDTO


def criarservice(criar_dto: CriarDTO):
    dados = criar_dto.__dict__

    return criar_repository(dados)
