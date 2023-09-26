#! /home/gitpod/.pyenv/shims/tutorial-env python3
""" Exibe relatório de crianças por atividade

Imprimir a lista de crianças agrupada por aula
que frenquentas cada uma das atividades
"""
__version__ ='0.1.0'

# Dados
sala1 = ["Erik","Maia","Gustavo","Manuel","Sofia","Joana"]
sala2 = ["Joao","Antonio","Carlos","Maria","Isolda"]

aula_ingles =["Erik","Maia","Antonio","Carlos","Joana"]
aula_musica=["Erik","Maria","Carlos"]
aula_danca=["Gustavo","Sofia","Joana","Antonio"]

atividade = [
    ("Ingles",aula_ingles),
    ("dança",aula_danca),
    ("musica",aula_musica)]

# Listar alunos em cada atividade por sala
for nome_atividade, atividade in atividade:

    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 40)
    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
            if aluno in sala1:
                atividade_sala1.append(aluno)
            elif aluno in sala2:
                atividade_sala2.append(aluno)

    print("Sala1",atividade_sala1)
    print("Sala2",atividade_sala2)
    print()
    print("#" * 40)