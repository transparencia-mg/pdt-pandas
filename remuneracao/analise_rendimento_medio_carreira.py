from frictionless import Package
import requests
import json
import pandas as pd

conjunto = 'remuneracao-servidores-ativos'
despesas_dataset = requests.get(f'https://dados.mg.gov.br/api/3/action/package_show?id={conjunto}')
despesas_dataset = despesas_dataset.json()
resources = despesas_dataset['result']['resources']
remuneracoes = [x for x in resources if x['url'].split('/')[-1].startswith('servidores-')]
datapackage_url = [x for x in resources if x['url'].split('/')[-1].startswith('datapackage')]
datapackage_url = datapackage_url[0]['url']
datapackage = requests.get(datapackage_url)
datapackage = datapackage.json()
package = Package(datapackage)

df = []
for resource in remuneracoes:
	resource_name = resource['url'].split('/')[-1].split('.')[0]
	split_resource_name = resource_name.split('-')
	year = split_resource_name[1]
	month = split_resource_name[2]
	package_resource = package.get_resource(resource_name)
	package_resource.path = resource['url']
	package_resource = package_resource.to_pandas()
	grouped = package_resource.groupby('nmefet')	
	grouped_salary_avg = grouped['rem_pos'].mean()
	resource_df = grouped_salary_avg.to_frame()
	resource_df = resource_df.reset_index()
	resource_df['year'] = year
	resource_df['month'] = month
	df.to_csv(file_name, sep='\t', encoding='utf-8')
	df.append(resource_df)

df = pd.concat(df)
df_grouped = df.groupby('nmefet')
df_grouped_salary_avg = df_grouped['rem_pos'].mean()
result = df_grouped_salary_avg.sort_values(ascending=False)
result = result.to_frame()
result = result.reset_index()
print(result)
import ipdb; ipdb.set_trace(context=10)



	