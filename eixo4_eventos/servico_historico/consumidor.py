import json
import time

ARQUIVO_FILA = "fila.txt"

print("Consumidor iniciado...")

processados = 0

while True:
    with open(ARQUIVO_FILA, "r") as fila:
        linhas = fila.readlines()

    novos_eventos = linhas[processados:]

    for linha in novos_eventos:
        evento = json.loads(linha)
        print("\nEvento recebido: ")
        print(evento)


        processados += 1
    time.sleep(5)