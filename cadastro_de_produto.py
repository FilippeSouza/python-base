#!/usr/bin/env python3

"""Cadastro de produto"""

__version__ = "0.1.1"



produto = {
	"nome": "Caneta",
	"cor1": "azul",
	"cor2": "branco",
	"preco": 3.23,
	"dimensao" : {"altura": 12.1, "largura": 12.1},
	"em_estoque": True,
	"codigo": 45678,
	"codebar": None,
}

cliente = {
	"nome": "Bruno"
}

compra = {
	"cliente": cliente,
	"produto": produto,
	"quantidade": 3
}

#print(compra)

total_compra = compra["quantidade"] * compra["produto"]["preco"]

print(
    f"O cliente {compra['cliente']['nome']}"
    f" comprou {compra['quantidade']} unidades de {compra['produto']['nome']}"
    f" e pagou o total de {total_compra}"
)
