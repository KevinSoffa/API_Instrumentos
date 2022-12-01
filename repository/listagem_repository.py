from models.dao.project import PROJECT
from models.dao.mongo import db
from math import ceil


def listagem_repository(listagem_dto: dict):
    #Colocando paginação na consulta
    total = db.instrumento.count_documents(
        {}
    )
    limite = 0

    if listagem_dto['paginacao_limite'] != 0:
        paginas = ceil(total / listagem_dto['paginacao_limite'])
    else:
        paginas = 1
        limite = total

    #GET no DB
    response = db.instrumento.find(
        {},
        PROJECT
    ).limit(
        listagem_dto['paginacao_limite']
    ).skip(
        (listagem_dto['paginacao_pagina']) * listagem_dto['paginacao_limite']
    )

    return {
        'total': total,
        'paginas': paginas,
        'pagina': listagem_dto['paginacao_pagina'],
        'limite': limite,
        'itens': list(response)
    }
