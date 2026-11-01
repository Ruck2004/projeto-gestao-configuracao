"""Gera um resumo quantitativo das tarefas do projeto."""
import csv
from collections import Counter
from pathlib import Path

ARQUIVO = Path(__file__).with_name("tarefas.csv")

def gerar_resumo():
    with ARQUIVO.open("r", encoding="utf-8", newline="") as arquivo:
        tarefas = list(csv.DictReader(arquivo))
    contagem = Counter(item["status"] for item in tarefas)
    print("RESUMO DO PROJETO")
    print(f"Total de tarefas: {len(tarefas)}")
    for status, quantidade in sorted(contagem.items()):
        print(f"{status}: {quantidade}")

if __name__ == "__main__":
    gerar_resumo()
