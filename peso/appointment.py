# Pesos definidos para cada tipo de task
TASK_WEIGHTS = {
    "Complete": 5,
    "Requirement": 1,
}

dates_list = ['2025-02-21', '2025-02-22']

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
    
model_peso = {}

date_model_percent = {}

def calcular_peso(tasks):
    global model_peso
    for bsc, (model, type_task) in tasks.items():
        if model not in model_peso:
            model_peso[model] = 0
    
        for type_TASK_WEIGHTS in TASK_WEIGHTS:
            if type_TASK_WEIGHTS == type_task:
                peso = TASK_WEIGHTS[type_TASK_WEIGHTS]
                model_peso[model] += peso
    return model_peso

def regra_de_tres(data):
    global date_model_percent
    total_peso_model = sum(data[model] for model in data)
    for model in data:
        model_percent = data[model] / total_peso_model * 100
        for date in dates_list:
            if date not in date_model_percent:
                date_model_percent[date] = {}
            date_model_percent[date][model] = round(model_percent)

model_peso_result = calcular_peso(tasks)
regra_de_tres(model_peso_result)

print(date_model_percent)

''' RETORNAR O SEGUINTE DICIONARIO: 
{
    'date': {
        'model': 'percent'
    },
    'date':{
        'model': 'percent'
    }
}

RETORNOU:

{
    '2025-02-21': {
        'A': 57,
        'S': 29,
        'X': 14
    }, 
    '2025-02-22': {
        'A': 57,
        'S': 29,
        'X': 14
    }
}

'''
