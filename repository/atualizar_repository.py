from models.dao.project import PROJECT
from models.dao.mongo import db
from bson import ObjectId


def atualizar_repository(id: str, dto: dict):
    return db.instrumento.find_one_and_update(
        {'_id': ObjectId(id)},
        {'$set': dto},
        PROJECT,
        return_document=True
    )