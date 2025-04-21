"""
Exibe relatorio de atividades de cada sala

Imprimir a lista de criancas agrupadas por sala
que frequentam cada atividade.

"""
__version__ = "0.1.0"
__author__ = "Davi Nascimento"

# Dados da escola
sala1 = ["Ana", "Alana", "Davi"]
sala2 = ["Joao", "Maria", "Pedro"]

aula_ingles = ["Ana", "Joao", "Maria"]
aula_musica = ["Alana", "Pedro", "Ana"]
aula_programacao = ["Davi", "Joao", "Maria"]

atividades = [
    ("ingles", aula_ingles),
    ("musica", aula_musica),
    ("programacao", aula_programacao),
]

# Imprime as atividades de cada sala com desempacotamento de tuplas
for nome_atividade, atividade in atividades:

    print(f"alunos da atividade {nome_atividade}\n")
    print("-" * 40)

    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)

    print("Sala 1", atividade_sala1)
    print("Sala 2", atividade_sala2)

    print("\n")
    print("#" * 40)
