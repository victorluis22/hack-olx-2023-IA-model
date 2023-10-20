import pandas as pd
import joblib
from sklearn import preprocessing

def randomForestPredict():
    """Função que usa o input da API para prever se os dados passados possuem probabilidade de golpe ou não."""
    tabela_previsao = pd.read_csv('apiTest.csv')
    loaded_rf = joblib.load("./randomForest.joblib")
    codes = joblib.load("./preprocessorCodes.joblib")

    transformedData2 = codes.transform(tabela_previsao[["Marca", "Modelo", "Condicao", "Bateria", "Golpe"]])

    resultData2 = pd.DataFrame(
        {
            "Marca": transformedData2[:, 0],
            "Modelo": transformedData2[:, 1],
            "Condicao": transformedData2[:, 2],
            "Memoria": tabela_previsao["Memoria"],
            "Bateria": transformedData2[:, 3],
            "Preco": tabela_previsao["Preco"],
            "TempoConta": tabela_previsao["TempoConta"],
            "Vendas": tabela_previsao["Vendas"],	
            "Golpe": transformedData2[:, 4]
        }
    )

    return loaded_rf.predict(resultData2[["Marca", "Modelo", "Condicao", "Memoria","Bateria", "Preco", "TempoConta", "Vendas"]])
