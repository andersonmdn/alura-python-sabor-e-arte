
from rich.console import Console
from fastapi import FastAPI, HTTPException
from typing import List
from schemas import Restaurante, RestauranteCreate, Avaliacao, AvaliacaoCreate

from database import criar_conexao, criar_tabelas, get_connection, fechar_conexao

console = Console()


conn = criar_conexao()
criar_tabelas(conn)
fechar_conexao(conn)

app = FastAPI(title="Gerenciamento de Restaurantes")

@app.get("/restaurantes/", response_model=List[Restaurante])
def listar_restaurantes(skip: int = 0, limit: int = 10):
    """Lista todos os restaurantes com paginação."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM restaurante LIMIT ? OFFSET ?", (limit, skip))
    rows = cursor.fetchall()
    fechar_conexao(conn)

    restaurantes = [
        Restaurante(id=row[0], nome=row[1], categoria=row[2], ativo=bool(row[3])) for row in rows
    ]
    return restaurantes

@app.get("/restaurantes/{restaurante_id}", response_model=Restaurante)
def buscar_restaurante(restaurante_id: int):
    """Busca um restaurante específico pelo ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM restaurante WHERE id = ?", (restaurante_id,))
    row = cursor.fetchone()
    fechar_conexao(conn)

    if not row:
        raise HTTPException(status_code=404, detail="Restaurante não encontrado")

    return Restaurante(id=row[0], nome=row[1], categoria=row[2], ativo=bool(row[3]))

@app.post("/restaurantes/", response_model=Restaurante)
def criar_restaurante(restaurante: RestauranteCreate):
    """Cria um novo restaurante."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO restaurante (nome, categoria, ativo) VALUES (?, ?, ?)",
        (restaurante.nome, restaurante.categoria, int(restaurante.ativo))
    )
    conn.commit()
    restaurante_id = cursor.lastrowid
    fechar_conexao(conn)

    return Restaurante(id=restaurante_id, **restaurante.dict())

@app.put("/restaurantes/{restaurante_id}", response_model=Restaurante)
def atualizar_restaurante(restaurante_id: int, restaurante: RestauranteCreate):
    """Atualiza os dados de um restaurante."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM restaurante WHERE id = ?", (restaurante_id,))
    row = cursor.fetchone()

    if not row:
        fechar_conexao(conn)
        raise HTTPException(status_code=404, detail="Restaurante não encontrado")

    cursor.execute(
        "UPDATE restaurante SET nome = ?, categoria = ?, ativo = ? WHERE id = ?",
        (restaurante.nome, restaurante.categoria, int(restaurante.ativo), restaurante_id)
    )
    conn.commit()
    fechar_conexao(conn)

    return Restaurante(id=restaurante_id, **restaurante.dict())

@app.delete("/restaurantes/{restaurante_id}")
def deletar_restaurante(restaurante_id: int):
    """Deleta um restaurante pelo ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM restaurante WHERE id = ?", (restaurante_id,))
    row = cursor.fetchone()

    if not row:
        fechar_conexao(conn)
        raise HTTPException(status_code=404, detail="Restaurante não encontrado")

    cursor.execute("DELETE FROM restaurante WHERE id = ?", (restaurante_id,))
    conn.commit()
    fechar_conexao(conn)

    return {"mensagem": "Restaurante deletado com sucesso"}

@app.post("/avaliacoes/", response_model=Avaliacao)
def criar_avaliacao(avaliacao: AvaliacaoCreate):
    """Cria uma nova avaliacao."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO avaliacao (cliente, nota, restaurante_id) VALUES (?, ?, ?)",
        (avaliacao.cliente, int(avaliacao.nota), int(avaliacao.id_restaurante))
    )
    conn.commit()
    avaliacao_id = cursor.lastrowid
    fechar_conexao(conn)

    return Avaliacao(id=avaliacao_id, **avaliacao.dict())

# @app.post("/avaliacoes/", response_model=Prato)
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
