from repository import detalhe_repository
from fastapi import HTTPException
from bson import ObjectId


def detalhe_service(id: ObjectId):
    response = detalhe_repository(
        str(id)
    )
    
    if response:
        return response
    print(response)

    raise HTTPException(400)