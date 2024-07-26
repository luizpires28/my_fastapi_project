#testando automação

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, database
from pydantic import BaseModel

app = FastAPI()

database.Base.metadata.create_all(bind=database.engine)

class PessoaCreate(BaseModel):
    nome: str
    idade: int

class PessoaResponse(BaseModel):
    id: int
    nome: str
    idade: int

    class Config:
        orm_mode = True

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/pessoa/", response_model=PessoaResponse)
def create_pessoa(pessoa: PessoaCreate, db: Session = Depends(get_db)):
    db_pessoa = models.Pessoa(nome=pessoa.nome, idade=pessoa.idade)
    db.add(db_pessoa)
    db.commit()
    db.refresh(db_pessoa)
    return db_pessoa

@app.get("/lista/", response_model=list[PessoaResponse])
def list_pessoas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    pessoas = db.query(models.Pessoa).offset(skip).limit(limit).all()
    return pessoas
