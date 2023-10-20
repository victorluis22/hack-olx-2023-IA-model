import random
import csv

# Definindo as opções disponíveis
marcas = ["Apple"]
modelos_apple = ["iPhone 8 Plus", "iPhone 11", "iPhone 10", "iPhone 12", "iPhone 13", "iPhone 14", "iPhone 15", "iPhone XR"]
condicoes = ["Novo", "Usado - Excelente", "Usado - Bom", "Recondicionado", "Com defeito"]
baterias = ["Perfeita (95% ate 100%)", "Boa (80% ate 94%)", "Ok (60% ate 79%)", "Ruim (40% ate 59%)", "Muito Ruim (abaixo de 39%)"]
memorias = [32, 64, 128, 256, 512]

# Variáveis para contagem de 'Sim' e 'Não'
contador_sim = 0
contador_nao = 0

# Criação do arquivo CSV
with open('train.csv', 'w', newline='') as csvfile:
    fieldnames = ['Marca', 'Modelo', 'Condicao', 'Memoria', 'Bateria', 'Preco', 'TempoConta', 'Vendas', 'Golpe']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for _ in range(200000):
        marca = random.choice(marcas)
        modelo = random.choice(modelos_apple)
        preco = random.uniform(0, 5000)
        condicao = random.choice(condicoes)
        memoria = random.choice(memorias)
        tempo = random.randint(1, 365)
        venda = random.randint(1, 20)
        bateria = random.choice(baterias)

        golpe = "Nao"

        if modelo == "iPhone 8 Plus":
            if memoria < 64 or memoria > 256 or preco < 300 or preco > 2000 or tempo < 10:
                golpe = "Sim"
        elif modelo == "iPhone 11":
            if memoria < 64 or memoria > 256 or preco < 800 or preco > 3000 or tempo < 10:
                golpe = "Sim"
        elif modelo == "iPhone 10":
            if memoria < 64 or memoria == 128 or memoria > 256 or preco < 500 or preco > 2000 or tempo < 10:
                golpe = "Sim"
        elif modelo == "iPhone 12":
            if memoria < 64 or memoria > 256 or preco < 800 or preco > 4000 or tempo < 10:
                golpe = "Sim"
        elif modelo == "iPhone 13":
            if memoria < 128 or memoria > 512 or preco < 1000 or preco > 5000 or tempo < 10:
                golpe = "Sim"
        elif modelo == "iPhone 14":
            if memoria < 128 or memoria > 512 or preco < 1500 or preco > 5000 or tempo < 10:
                golpe = "Sim"
        elif modelo == "iPhone 15":
            if memoria < 128 or memoria > 512 or preco < 4000 or tempo < 10:
                golpe = "Sim"
        elif modelo == "iPhone XR":
            if memoria < 64 or memoria > 256 or preco < 800 or preco > 2000 or tempo < 10:
                golpe = "Sim"

        # Atualizar contadores
        if golpe == "Sim":
            contador_sim += 1
        else:
            contador_nao += 1

        writer.writerow({
            'Marca': marca,
            'Modelo': modelo,
            'Condicao': condicao,
            'Memoria': memoria,
            'Bateria': bateria,
            'Preco': round(preco, 2),
            'TempoConta': tempo,
            'Vendas': venda,
            'Golpe': golpe
        })
# Imprimir contagens
print(f"Quantidade de 'Sim' para Golpe: {contador_sim}")
print(f"Quantidade de 'Nao' para Golpe: {contador_nao}")