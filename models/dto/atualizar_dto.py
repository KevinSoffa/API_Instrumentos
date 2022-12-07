from pydantic import (
    Field,
    BaseModel
)


class AtualizarDTO(BaseModel):
    nome_instrumento: str = Field(None)
    marca: str = Field(None)
    modelo: str = Field(None)
    est_preco: int = Field(None)
    obs: str = Field(None),
    orquestra: bool = Field(None)
