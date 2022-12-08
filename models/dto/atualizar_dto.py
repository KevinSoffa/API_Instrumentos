from pydantic import (
    Field,
    BaseModel
)


class AtualizarDTO(BaseModel):
    nome_instrumento: str = Field(...)
    marca: str = Field(...)
    modelo: str = Field(...)
    est_preco: int = Field(...)
    obs: str = Field(...)
    orquestra: bool = Field(...)
