
#!/usr/bin/env python3
"""
Exibir Relatorio de crianças por atividade.


Imprimir a lista  de crianças agrupadas  por sala que frequentas cada uma das atividades



"""
__version__= "0.1.0"

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

#Requirimentos

aula_ingles_sala1 = []
aula_ingles_sala2 =  []
aula_musica_sala1 = []
aula_musica_sala2 = []
aula_danca_sala1 = []
aula_danca_sala2 = []
for aluno in  aula_ingles:
	if aluno  in sala1:
		aula_ingles_sala1.append(aluno)
	elif aluno in sala2:
		aula_ingles_sala2.append(aluno)
for aluno in aula_musica:
	if aluno in sala1:
		aula_musica_sala1.append(aluno)
	elif aluno in sala2:
		aula_musica_sala2.append(aluno)
for aluno in aula_danca:
	if aluno in sala1:
		aula_danca_sala1.append(aluno)
	elif aluno in sala2:
		aula_danca_sala2.append(aluno)
print("Ingles Sala 1", aula_ingles_sala1)
print("Ingles Sala 2", aula_ingles_sala2)
print("Musica sala 1", aula_musica_sala1)
print("Musica sala 2", aula_musica_sala2)
print("Danca sala 1", aula_danca_sala1)
print("Danca sala 2", aula_danca_sala2)



