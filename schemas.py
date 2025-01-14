from pydantic import BaseModel

class RestauranteBase(BaseModel):
    nome: str
    categoria: str
    ativo: bool = True

class RestauranteCreate(RestauranteBase):
    pass

class Restaurante(RestauranteBase):
    id: int

    class Config:
        orm_mode = True
        
class AvaliacaoBase(BaseModel):
    cliente: str
    nota: int
    id_restaurante: int

class AvaliacaoCreate(AvaliacaoBase):
    pass

class Avaliacao(AvaliacaoBase):
    id: int

    class Config:
        orm_mode = True