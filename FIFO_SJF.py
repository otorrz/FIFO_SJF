# Lista de processos (nome, tempo de execução)
processos = [
    ("p1", 5),
    ("p2", 3),
    ("p3", 8)
]

# ---------------- FIFO (First In First Out) ----------------
def fifo(processos):
    tempo_total = 0
    tempos_espera = []
    tempos_turnaround = []

    for nome, tempo in processos:
        tempos_espera.append(tempo_total)
        tempo_total += tempo
        tempos_turnaround.append(tempo_total)

    return tempos_espera, tempos_turnaround

# ---------------- SJF (Shortest Job First) ----------------
def sjf(processos):
    processos_ordenados = sorted(processos, key=lambda x: x[1])

    tempo_total = 0
    tempos_espera = []
    tempos_turnaround = []

    for nome, tempo in processos_ordenados:
        tempos_espera.append(tempo_total)
        tempo_total += tempo
        tempos_turnaround.append(tempo_total)

    return processos_ordenados, tempos_espera, tempos_turnaround

# ---------------- Execução ----------------

# FIFO
print("=== FIFO ===")
espera_fifo, turnaround_fifo = fifo(processos)

for i, (nome, _) in enumerate(processos):
    print(f"{nome} - Espera: {espera_fifo[i]} | Turnaround: {turnaround_fifo[i]}")

# SJF
print("\n=== SJF ===")
processos_sjf, espera_sjf, turnaround_sjf = sjf(processos)

for i, (nome, _) in enumerate(processos_sjf):
    print(f"{nome} - Espera: {espera_sjf[i]} | Turnaround: {turnaround_sjf[i]}")


    # No caso o FIFO executa por oden de chegada 
    # já o SJF ordena pelo tempo do processo 
    # turnaround seria o tempo toal da exec