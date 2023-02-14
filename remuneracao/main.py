import pandas as pd

# Leitura recurso "Remuneração de Novembro de 2021" - https://dados.mg.gov.br/dataset/remuneracao-servidores-ativos/resource/999eb55f-df3b-4e7d-a3a5-43ebdc14aca3?inner_span=True
remuneracao_202211 = pd.read_csv('https://dados.mg.gov.br/dataset/98b58ea9-813e-4f50-8555-4ec0e15bbe91/resource/999eb55f-df3b-4e7d-a3a5-43ebdc14aca3/download/servidores-2021-11.csv.gz', encoding='cp1252', delimiter=";")

# Visualização das primeiras 5 linhas/registros da tabela "Remuneração de Novembro de 2022":
print(remuneracao_202211.head())
