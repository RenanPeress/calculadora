TASK_WEIGHTS = {
    "Complete": 5,
    "Requirement": 1,
}

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

def calcular_percentuais(tasks_por_dia):
    model_date_percent = {}

    for date, tasks in tasks_por_dia.items():
        model_peso = {}

        # Calcula o peso total de cada modelo para o dia atual
        for _, (model, type_task) in tasks.items():
            model_peso[model] = model_peso.get(model, 0) + TASK_WEIGHTS.get(type_task, 0)

        total_peso = sum(model_peso.values())
        if total_peso == 0:
            continue  # Evita divisão por zero

        # Calcula a porcentagem de cada modelo e armazena corretamente no formato solicitado
        for model, peso in model_peso.items():
            if model not in model_date_percent:
                model_date_percent[model] = {}  # Inicializa o dicionário para o modelo
            model_date_percent[model][date] = round((peso / total_peso) * 100)

    return model_date_percent

# Executa a função e imprime o resultado
model_date_percent = calcular_percentuais(tasks_por_dia)
print(model_date_percent)
