from models.dao.project import PROJECT
from models.dao.mongo import db
from bson import ObjectId


def atualizar_repository(id: ObjectId, models_dto: dict):
    return db.instrumento.find_one_and_update(
        {'_id': ObjectId(id)},
        {'$set': models_dto},
        PROJECT,
        return_document=True
    )
