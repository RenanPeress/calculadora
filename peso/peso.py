from collections import defaultdict

# Pesos definidos para cada tipo de task
TASK_WEIGHTS = {
    "A": 10,
    "B": 20,
    "C": 30,
    "D": 40
}

def calcular_porcentagem_tasks(tasks):
    """
    Calcula a porcentagem correta para cada device baseado nos tipos de tasks.
    
    :param tasks: Lista de dicionários representando tasks, ex.:
        [
            {"device": "X", "tipo": "A"},
            {"device": "Y", "tipo": "B"},
            {"device": "Z", "tipo": "C"},
            {"device": "W", "tipo": "D"},
        ]
    :return: Dicionário com o device e a porcentagem correta.
    """
    # Agrupa as tasks por device e tipo
    device_task_counts = defaultdict(lambda: defaultdict(int))
    for task in tasks:
        device_task_counts[task["device"]][task["tipo"]] += 1

    # Calcula o total de peso
    total_peso = sum(TASK_WEIGHTS[task["tipo"]] for task in tasks)

    # Calcula a porcentagem final para cada device
    device_percentages = {}
    for device, tipos in device_task_counts.items():
        total_peso_device = sum(TASK_WEIGHTS[tipo] * count for tipo, count in tipos.items())
        device_percentages[device] = round((total_peso_device / total_peso) * 100, 2)

    return device_percentages

# Exemplo de entrada com tasks de diferentes tipos
tasks = [
    {"device": "X", "tipo": "A"},
    {"device": "X", "tipo": "A"},
    {"device": "X", "tipo": "A"},
    {"device": "X", "tipo": "A"},
    {"device": "X", "tipo": "A"},
    {"device": "Z", "tipo": "B"},
    {"device": "Z", "tipo": "B"},
    {"device": "Z", "tipo": "B"},
    {"device": "Z", "tipo": "B"},
    {"device": "Z", "tipo": "B"},
    {"device": "Y", "tipo": "C"},
    {"device": "Y", "tipo": "C"},
    {"device": "Y", "tipo": "C"},
    {"device": "Y", "tipo": "C"},
    {"device": "Y", "tipo": "C"},
    {"device": "W", "tipo": "D"},
    {"device": "W", "tipo": "D"},
    {"device": "W", "tipo": "D"},
    {"device": "W", "tipo": "D"},
    {"device": "W", "tipo": "D"},
]

# Testando a função
porcentagem_final = calcular_porcentagem_tasks(tasks)
print(porcentagem_final)