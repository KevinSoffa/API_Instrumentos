from models.dao.project import PROJECT
from models.dao.mongo import db


def criar_repository(dto: dict):
    db.instrumento.insert_one(
        dto
    )

    dto['id'] = str(dto.pop('_id'))

    return dto
