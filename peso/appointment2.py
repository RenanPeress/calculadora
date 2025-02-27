TASK_WEIGHTS = {
    "Complete": 5,
    "Requirement": 1,
}
dates_list = ['2025-02-21', '2025-02-22']
model_peso = {}
model_date_percent = {}

tasks = {
    'BSC-1': ['A', 'Complete'],
    'BSC-2': ['A', 'Complete'],
    'BSC-3': ['A', 'Requirement'],
    'BSC-4': ['A', 'Complete'],
    'BSC-6': ['S', 'Requirement'],
    'BSC-5': ['S', 'Requirement'],
    'BSC-7': ['S', 'Requirement'],
    'BSC-8': ['S', 'Complete'],
    'BSC-9': ['X', 'Requirement'],
    'BSC-10': ['X', 'Requirement'],
    'BSC-11': ['X', 'Requirement'],
    'BSC-12': ['X', 'Requirement']
}

def calcular_peso(tasks):
    global model_peso
    for bsc, (model, type_task) in tasks.items():
        if model not in model_peso:
            model_peso[model] = 0
    
        if type_task in TASK_WEIGHTS:
            model_peso[model] += TASK_WEIGHTS[type_task]
    
    return model_peso

def regra_de_tres(data):
    global model_date_percent
    total_peso_model = sum(data.values())

    for model in data:
        model_percent = data[model] / total_peso_model * 100
        model_date_percent[model] = {}  # Inicializa corretamente para cada modelo

        for date in dates_list:
            model_date_percent[model][date] = round(model_percent)

# Chamando as funções para gerar os valores
pesos = calcular_peso(tasks)
regra_de_tres(pesos)

print(model_date_percent)