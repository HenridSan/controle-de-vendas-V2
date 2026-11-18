import pytest

from logica import custo_total, custo_por_unidade, unidades_vendidas, restantes, total_recebido, lucro_em_vendas, caixa

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


def vendas_de_exemplo():
    return [
        {"id": 1, "produto_id": 1, "data": "2026-11-10", "quantidade": 1, "preco": 8.0},
        {"id": 2, "produto_id": 1, "data": "2026-11-12", "quantidade": 2, "preco": 8.0},
        {"id": 3, "produto_id": 1, "data": "2026-11-15", "quantidade": 1, "preco": 10.0},
        {"id": 4, "produto_id": 2, "data": "2026-11-15", "quantidade": 5, "preco": 35.0},
    ]


def test_unidade_vendidas_soma_soma_produto():
    assert unidades_vendidas(novo_bolo(), vendas_de_exemplo()) == 4


def test_unidade_vendidas_sem_venda():
    assert unidades_vendidas(novo_bolo(), []) == 0


def test_restantes():
    assert restantes(novo_bolo(), vendas_de_exemplo()) == 6


def test_restantes_sem_venda():
    assert restantes(novo_bolo(), []) == 10


def test_total_recebido_vendendo_usa_venda():
    assert total_recebido(novo_bolo(), vendas_de_exemplo()) == 34.0


def test_total_recebido_sem_venda():
    assert total_recebido(novo_bolo(), []) == 0


def test_caixa_comeca_negativa():
    assert caixa(novo_bolo(), gasto_por_exemplo(), []) == -17.0


def test_caixa_com_venda():
    assert caixa(novo_bolo(), gasto_por_exemplo(), vendas_de_exemplo()) == 17.0


def test_lucro_em_venda_sem_venda():
    assert lucro_em_vendas(novo_bolo(), gasto_por_exemplo(), []) == 0


def test_lucro_em_venda_vendendo():
    lucro = lucro_em_vendas(novo_bolo(), gasto_por_exemplo(), vendas_de_exemplo())
    assert lucro == pytest.approx(27.2)


def test_caixa_e_lucro_em_vendas():
    bolo = novo_bolo()
    gasto = gasto_por_exemplo()
    venda = vendas_de_exemplo()
    custo_sobra = restantes(bolo, venda) * custo_por_unidade(bolo, gasto)
    esperado = lucro_em_vendas(bolo, gasto, venda) - custo_sobra
    assert caixa(bolo, gasto, venda) == pytest.approx(esperado)
