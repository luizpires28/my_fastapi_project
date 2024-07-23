from sqlalchemy import Column, Integer, String
from .database import Base
from pydantic import BaseModel

# Modelo do SQLAlchemy
class Pessoa(Base):
    __tablename__ = 'pessoas'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    idade = Column(Integer)

# Modelos Pydantic
class PessoaBase(BaseModel):
    nome: str
    idade: int

    class Config:
        from_attributes = True  # Substituir orm_mode por from_attributes

class PessoaCreate(PessoaBase):
    pass

class PessoaResponse(PessoaBase):
    id: int

    class Config:
        from_attributes = True  # Substituir orm_mode por from_attributes
