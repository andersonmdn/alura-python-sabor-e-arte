
from rich.console import Console
from fastapi import FastAPI, HTTPException
from typing import List
from schemas import Restaurante, RestauranteCreate, Avaliacao, AvaliacaoCreate

from database import DatabaseManager

console = Console()


db = DatabaseManager()

app = FastAPI(title="Gerenciamento de Restaurantes")

@app.get("/restaurantes/", response_model=List[Restaurante])
def listar_restaurantes(skip: int = 0, limit: int = 10):
    """Lista todos os restaurantes com paginação."""
    db.conectar()
    cursor = db.get_cursor()
    cursor.execute("SELECT * FROM restaurantes LIMIT ? OFFSET ?", (limit, skip))
    rows = cursor.fetchall()
    db.fechar_conexao()

    restaurantes = [
        Restaurante(id=row[0], nome=row[1], categoria=row[2], ativo=bool(row[3])) for row in rows
    ]
    return restaurantes

@app.get("/restaurantes/{restaurante_id}", response_model=Restaurante)
def buscar_restaurante(restaurante_id: int):
    """Busca um restaurante específico pelo ID."""
    db.conectar()
    cursor = db.get_cursor()
    cursor.execute("SELECT * FROM restaurantes WHERE id = ?", (restaurante_id,))
    row = cursor.fetchone()
    db.fechar_conexao()

    if not row:
        raise HTTPException(status_code=404, detail="Restaurante não encontrado")

    return Restaurante(id=row[0], nome=row[1], categoria=row[2], ativo=bool(row[3]))

@app.post("/restaurantes/", response_model=Restaurante, status_code=201)
def criar_restaurante(restaurante: RestauranteCreate):
    """Cria um novo restaurante."""
    db.conectar()
    cursor = db.get_cursor()
    cursor.execute(
        "INSERT INTO restaurantes (nome, categoria, ativo) VALUES (?, ?, ?)",
        (restaurante.nome, restaurante.categoria, int(restaurante.ativo))
    )
    db.commit()
    restaurante_id = cursor.lastrowid
    db.fechar_conexao()

    return Restaurante(id=restaurante_id, **restaurante.dict())

@app.put("/restaurantes/{restaurante_id}", response_model=Restaurante)
def atualizar_restaurante(restaurante_id: int, restaurante: RestauranteCreate):
    """Atualiza os dados de um restaurante."""
    db.conectar()
    cursor = db.get_cursor()
    cursor.execute("SELECT * FROM restaurantes WHERE id = ?", (restaurante_id,))
    row = cursor.fetchone()

    if not row:
        db.fechar_conexao()
        raise HTTPException(status_code=404, detail="Restaurante não encontrado")

    cursor.execute(
        "UPDATE restaurantes SET nome = ?, categoria = ?, ativo = ? WHERE id = ?",
        (restaurante.nome, restaurante.categoria, int(restaurante.ativo), restaurante_id)
    )
    db.commit()
    db.fechar_conexao()

    return Restaurante(id=restaurante_id, **restaurante.dict())

@app.delete("/restaurantes/{restaurante_id}")
def deletar_restaurante(restaurante_id: int):
    """Deleta um restaurante pelo ID."""
    db.conectar()
    cursor = db.get_cursor()
    cursor.execute("SELECT * FROM restaurantes WHERE id = ?", (restaurante_id,))
    row = cursor.fetchone()

    if not row:
        db.fechar_conexao()
        raise HTTPException(status_code=404, detail="Restaurante não encontrado")

    cursor.execute("DELETE FROM restaurantes WHERE id = ?", (restaurante_id,))
    db.commit()
    db.fechar_conexao()

    return {"mensagem": "Restaurante deletado com sucesso"}

@app.post("/avaliacoes/", response_model=Avaliacao, status_code=201)
def criar_avaliacao(avaliacao: AvaliacaoCreate):
    """Cria uma nova avaliacao."""
    db.conectar()
    cursor = db.get_cursor()
    cursor.execute(
        "INSERT INTO avaliacoes (cliente, nota, restaurante_id) VALUES (?, ?, ?)",
        (avaliacao.cliente, int(avaliacao.nota), int(avaliacao.id_restaurante))
    )
    db.commit()
    avaliacao_id = cursor.lastrowid
    db.fechar_conexao()

    return Avaliacao(id=avaliacao_id, **avaliacao.dict())

# @app.post("/pratos/", response_model=Prato)
# def criar_prato(prato: PratoCreate):
#     """Cria uma nova prato."""
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute(
#         "INSERT INTO prato (cliente, nota, restaurante_id) VALUES (?, ?, ?)",
#         (prato.cliente, int(prato.nota), int(prato.id_restaurante))
#     )
#     conn.commit()
#     prato_id = cursor.lastrowid
#     fechar_conexao(conn)

#     return Prato(id=prato_id, **prato.dict())
