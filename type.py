import pandas as pd

# carrega o arquivo CSV em um DataFrame
df = pd.read_csv('OtherNames_0_colunas.csv')

# itera sobre as colunas e imprime o datatype de cada uma
for col in df.columns:
    print(f"Coluna {col}: {df[col].dtype}")
