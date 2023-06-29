
#!/usr/bin/env python3
"""
Exibir Relatorio de crianças por atividade.


Imprimir a lista  de crianças agrupadas  por sala que frequentas cada uma das atividades



"""
__version__= "0.1.0"

# Dados
sala1 = {"alunos1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]}
sala2 = {"alunos2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]}

aula_ingles = {"ingles": ["Erik", "Maia", "Joana", "Carlos", "Antonio"]}
aula_musica = {"musica": ["Erik", "Carlos", "Maria"]}
aula_danca = {"danca": ["Gustavo", "Sofia", "Joana", "Antonio"]}

#Requirimentos
atividades = {"rotinas": ["Ingles","Musica", "Danca"]}


print(f"Os Alunos das atividades saAlunos da atividade{nome_atividade}\n")
	print("-" * 40)


	atividade_sala1 = set(sala1) & set(atividade)
	atividade_sala2 = set(sala2).intersection(atividade)

	print("sala1", atividade_sala1)
	print("sala2", atividade_sala2)

	print()
	print("#" * 40)
