TASK_WEIGHTS = {
    "Complete": 5,
    "Requirement": 1,
}

model_date_percent = {}

tasks_por_dia = {
    "2025-02-21": {
        'BSC-1': ['A', 'Complete'],
        'BSC-2': ['A', 'Complete'],
        'BSC-3': ['A', 'Requirement'],
        'BSC-6': ['S', 'Requirement'],
        'BSC-8': ['S', 'Complete'],
        'BSC-9': ['X', 'Requirement']
    },
    "2025-02-22": {
        'BSC-4': ['A', 'Complete'],
        'BSC-5': ['S', 'Requirement'],
        'BSC-7': ['S', 'Requirement'],
        'BSC-10': ['X', 'Requirement'],
        'BSC-11': ['X', 'Requirement'],
        'BSC-12': ['X', 'Requirement']
    }
}

def calcular_peso(tasks):
    """ Calcula o peso total de cada modelo com base nas tasks """
    model_peso = {}
    for _, (model, type_task) in tasks.items():
        if model not in model_peso:
            model_peso[model] = 0
        if type_task in TASK_WEIGHTS:
            model_peso[model] += TASK_WEIGHTS[type_task]
    
    return model_peso

def regra_de_tres(data, date):
    """ Calcula a porcentagem e armazena no formato desejado {modelo: {data: porcentagem}} """
    total_peso_model = sum(data.values())
    if total_peso_model == 0:
        return  # Evita divisão por zero

    for model in data:
        model_percent = data[model] / total_peso_model * 100
        if model not in model_date_percent:
            model_date_percent[model] = {}  # Inicializa o modelo corretamente
        model_date_percent[model][date] = round(model_percent)

# Processando cada dia separadamente
for date, tasks in tasks_por_dia.items():
    pesos = calcular_peso(tasks)
    regra_de_tres(pesos, date)

print(model_date_percent)
