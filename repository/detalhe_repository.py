from models.dao.project import PROJECT
from models.dao.mongo import db
from bson import ObjectId


def detalhe_repository(id: str):
    return db.instrumento.find_one(
        {'_id': ObjectId(id)},
        PROJECT
    )
