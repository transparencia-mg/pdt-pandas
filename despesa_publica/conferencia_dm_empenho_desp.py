import requests
import json
import pandas as pd

despesas_dataset = requests.get('https://dados.mg.gov.br/api/3/action/package_show?id=despesa')
despesas_dataset = despesas_dataset.json()
despesas_dict = despesas_dataset['result']
despesas_id = despesas_dict['id']
resources = [x['value'] for x in despesas_dict['extras'] if x['key'] == 'resources_ids'][0]
resources = json.loads(resources)
dm_empenhos = [x for x in resources if x.startswith('dm_empenho_desp')]


df = []
for resource in dm_empenhos:
	resouce_id = resources[resource]
	resource_url = f'https://dados.mg.gov.br/dataset/{despesas_id}/resource/{resouce_id}/download/{resource}.csv.gz'
	if isinstance(df, str):
		df = pd.read_csv(resource_url, delimiter=";")
	else:
		resource_df = pd.read_csv(resource_url, delimiter=";")
		df.append(resource_df)
	print(f'{resource} data frame created.')	
df = pd.concat(df)
print(f'Concat data frames')
grouped = df.groupby('ano_exercicio')
print(grouped['id_empenho'].count())