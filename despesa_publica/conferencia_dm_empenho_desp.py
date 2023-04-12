import requests
import json
import pandas as pd

despesas_dataset = requests.get('https://dados.mg.gov.br/api/3/action/package_show?id=despesa')
despesas_dataset = despesas_dataset.json()
resources = despesas_dataset['result']['resources']
dm_empenhos = [x for x in resources if x['url'].split('/')[-1].startswith('dm_empenho_desp')]

df = []
for resource in dm_empenhos:
	resource_df = pd.read_csv(resource['url'], delimiter=";")
	df.append(resource_df)
	print(f'{resource["name"]} data frame created.')	
df = pd.concat(df)
print(f'Concat data frames')
grouped = df.groupby('ano_exercicio')
print(grouped['id_empenho'].count())