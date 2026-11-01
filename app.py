import csv
from pathlib import Path

ARQUIVO = Path(__file__).with_name("tarefas.csv")

def carregar_tarefas():
    with ARQUIVO.open("r", encoding="utf-8", newline="") as arquivo:
        return list(csv.DictReader(arquivo))

def listar_tarefas():
    tarefas = carregar_tarefas()
    print("\nCONTROLE DE TAREFAS DA EQUIPE")
    print("-" * 58)
    for tarefa in tarefas:
        print(f"#{tarefa['id']} | {tarefa['titulo']} | {tarefa['responsavel']} | {tarefa['status']}")
    print("-" * 58)
    pendentes = sum(1 for tarefa in tarefas if tarefa["status"].lower() != "concluida")
    print(f"Total de tarefas: {len(tarefas)}")
    print(f"Tarefas ainda não concluídas: {pendentes}")

if __name__ == "__main__":
    listar_tarefas()
