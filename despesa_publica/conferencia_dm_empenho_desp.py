import requests
import json

despesas_dataset = requests.get('https://dados.mg.gov.br/api/3/action/package_show?id=despesa')
despesas_dataset = despesas_dataset.json()
despesas_dict = despesas_dataset['result']
despesas_id = despesas_dict['id']
resources = [x['value'] for x in despesas_dict['extras'] if x['key'] == 'resources_ids'][0]
resources = json.loads(resources)
dm_empenhos = [x for x in resources if x.startswith('dm_empenho_desp')]

import ipdb; ipdb.set_trace(context=10)
# resource_url = f'https://dados.mg.gov.br/dataset/{despesas_id}/resource/{resouce_id}/download/{resouce_name}.csv.gz'
