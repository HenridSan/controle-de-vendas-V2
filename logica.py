# logica.py
# Contas do aplicativo
# Tres tipos de fichas:
# {"id", "tipo", "nome", "receita", "preco", "quantidade"},
# {"id", "produto_id", "descricao", "valor"},
# {"id", "produto_id", "data", "quantidade", "preco"}

def custo_total(produto, gastos):
    total = 0
    for gasto in gastos:
        if gasto["produto_id"] == produto["id"]:
            total = total + gasto["valor"]
    return total


def custo_por_unidade(produto, gastos):
    if produto["quantidade"] <= 0:
        return 0
    return custo_total(produto, gastos) / produto["quantidade"]


def unidades_vendidas(produto, vendas):
    total = 0
    for venda in vendas:
        if venda["produto_id"] == produto["id"]:
            total = total + venda["quantidade"]
    return total


def restantes(produto, vendas):
    return produto["quantidade"] - unidades_vendidas(produto, vendas)


def total_recebido(produto, vendas):
    total = 0
    for venda in vendas:
        if venda["produto_id"] == produto["id"]:
            total = total + venda["quantidade"] * venda["preco"]
    return total


def caixa(produto, gastos, vendas):
    return total_recebido(produto, vendas) - custo_total(produto, gastos)


def lucro_em_vendas(produto, gastos, vendas):
    custo_unidade = custo_por_unidade(produto, gastos)
    total = 0
    for venda in vendas:
        if venda["produto_id"] == produto["id"]:
            total = total + venda["quantidade"] * (venda["preco"] - custo_unidade)
    return total


def criar_venda(produto, vendas, quantidade, hoje, preco=None):
    if quantidade <= 0:
        raise ValueError("A quantidade precisa ser maior que zero.")
    if preco is None:
        preco = produto["preco"]
    if preco <= 0:
        raise ValueError("O preço tem que ser maior que zero.")
    sobra = restantes(produto, vendas)
    if quantidade > sobra:
        raise ValueError(f"A quantidade precisa ser maior que {sobra}")
    return {
        "produto_id": produto["id"],
        "data": hoje.isoformat(),
        "quantidade": quantidade,
        "preco": preco,
    }