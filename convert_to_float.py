import pandas as pd


def convert_latitude():
    # Carrega o arquivo CSV
    df = pd.read_csv("OtherNames_0_colunas.csv")

    # Converte a coluna "latitude" para float
    df["latitude"] = df["latitude"].astype(str)

    # Salva o DataFrame de volta para o arquivo CSV
    df.to_csv("OtherNames_0_colunas.csv", index=False)


def convert_longitude():
    # Carrega o arquivo CSV
    df = pd.read_csv("OtherNames_0_colunas.csv")

    # Converte a coluna "latitude" para float
    df["longitude"] = df["longitude"].astype(str)

    # Salva o DataFrame de volta para o arquivo CSV
    df.to_csv("OtherNames_0_colunas.csv", index=False)
    print("longitude convertida")