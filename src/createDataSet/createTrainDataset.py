import random
import csv

# Definindo as opções disponíveis
marcas = ["Motorola", "Apple", "Samsung"]
modelos_motorola = ["Motorola G7", "Motorola Edge 30"]
modelos_apple = ["iPhone 8 Plus", "iPhone 11", "iPhone 10", "iPhone 12", "iPhone 13", "iPhone 14", "iPhone 15", "iPhone XR"]
modelos_samsung = ["Galaxy S20", "Galaxy S21", "Galaxy S22", "Galaxy A71", "Galaxy A51"]
condicoes = ["Novo", "Usado - Excelente", "Usado - Bom", "Recondicionado", "Com defeito"]
baterias = ["Perfeita (95% ate 100%)", "Boa (80% ate 94%)", "Ok (60% ate 79%)", "Ruim (40% ate 59%)", "Muito Ruim (abaixo de 39%)"]
memorias = [32, 64, 128, 256]
precos_apple = [random.uniform(300, 1500) for _ in range(200)]
precos_samsung = [random.uniform(300, 1500) for _ in range(200)]
precos_motorola = [random.uniform(300, 1500) for _ in range(200)]
tempo_conta = [random.randint(1, 365) for _ in range(200)]
vendas = [random.randint(1, 20) for _ in range(200)]

# Criação do arquivo CSV
with open('train.csv', 'w', newline='') as csvfile:
    fieldnames = ['Marca', 'Modelo', 'Condicao', 'Memoria', 'Bateria', 'Preco', 'TempoConta', 'Vendas', 'Golpe']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for _ in range(12000):
        marca = random.choice(marcas)
        if marca == "Apple":
            modelo = random.choice(modelos_apple)
            preco = random.choice(precos_apple)
        elif marca == "Motorola":
            modelo = random.choice(modelos_motorola)
            preco = random.choice(precos_motorola)
        else:
            modelo = random.choice(modelos_samsung)
            preco = random.choice(precos_samsung)

        condicao = random.choice(condicoes)
        memoria = random.choice(memorias)
        tempo = random.choice(tempo_conta)
        venda = random.choice(vendas)
        bateria = random.choice(baterias)

        if marca == "Apple" and memoria < 128:
            golpe = "Sim"
        elif marca == "Apple" and preco < 300:
            golpe = "Sim"
        elif tempo < 10:
            golpe = "Sim"
        elif venda > 10:
            golpe = "Nao"
        else:
            golpe = "Nao"

        writer.writerow({
            'Marca': marca,
            'Modelo': modelo,
            'Condicao': condicao,
            'Memoria': memoria,
            'Bateria': bateria,
            'Preco': round(preco,2),
            'TempoConta': tempo,
            'Vendas': venda,
            'Golpe': golpe
        })