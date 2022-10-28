import pandas as pd

# Leitura recurso "Compras" - https://dados.mg.gov.br/dataset/compras_contratos/resource/eff6e8a5-0913-44f2-a686-4178cd9c54a1
compras = pd.read_csv('https://dados.mg.gov.br/dataset/86e157db-d2c5-4151-9b16-9c5987462cba/resource/eff6e8a5-0913-44f2-a686-4178cd9c54a1/download/ft_compras.csv.gz', delimiter=";")

# Leitura recurso "Tipo Licitação" - https://dados.mg.gov.br/dataset/compras_contratos/resource/1c227c87-477e-427b-9c8f-1dee926e5c0a
tipo_licitacao = pd.read_csv('https://dados.mg.gov.br/dataset/86e157db-d2c5-4151-9b16-9c5987462cba/resource/1c227c87-477e-427b-9c8f-1dee926e5c0a/download/dm_tipo_licitacao.csv.gz', delimiter=";")

# Merge (Inner Join) dos dois recursos via campo em comum "id_tipo_licitacao"
compras_contratos = pd.merge(compras, tipo_licitacao)

# Visualização das primeiras 5 linhas/registros da tabela unificada "compras_contratos"
print(compras_contratos.head())
