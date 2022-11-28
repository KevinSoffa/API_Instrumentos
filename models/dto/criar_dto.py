from pydantic import (
    Field,
    BaseModel
)


class CriarDTO(BaseModel):
    nome_instrumento: str = Field(...)
    marca: str = Field(...)
    modelo: str = Field(...)
    est_preco: int = Field(...)
    obs: str = Field(None),
    orquestra: bool = Field(...)
