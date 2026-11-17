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
