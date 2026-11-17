import pytest

from logica import custo_total, custo_por_unidade

def novo_bolo():
    return {
    "id": 1,
    "tipo": "comida",
    "nome": "bolo de cenoura",
    "receita": "bater a massa do bolo e assar durante 40 min",
    "preco": 8.0,
    "quantidade": 10
    }


def gasto_por_exemplo():
    return [
        {"id": 1, "produto_id": 1, "descricao": "cenoura", "valor": 4.0},
        {"id": 2, "produto_id": 1, "descricao": "ovo", "valor": 8.0},
        {"id": 3, "produto_id": 1, "descricao": "farinha", "valor": 5.0},
        {"id": 4, "produto_id": 2, "descricao": "fone", "valor": 200.0},
    ]


def test_custo_total_soma_dos_gastos():
    assert custo_total(novo_bolo(), gasto_por_exemplo()) == 17.0


def test_custo_total_sem_gastos():
    assert custo_total(novo_bolo(), []) == 0


def test_custo_por_unidade():
    assert custo_por_unidade(novo_bolo(), gasto_por_exemplo()) == pytest.approx(1.7)


def test_custo_por_unidade_quantidade_zero():
    bolo = novo_bolo()
    bolo["quantidade"] = 0
    assert custo_por_unidade(bolo, novo_bolo()) == 0