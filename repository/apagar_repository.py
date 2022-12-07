from models.dao.mongo import db
from bson import ObjectId


def apagar_repository(id: str):
    return db.instrumento.find_one_and_delete(
        {'_id': ObjectId(id)}
    )
