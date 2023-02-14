from datetime import datetime
from frictionless import Package
import pandas as pd

# Data
now = datetime.now()
today = now.strftime('%Y%m%d')
today = str(today)

# Using frictionless to filter fhemig
# package = Package('https://dados.mg.gov.br/dataset/98b58ea9-813e-4f50-8555-4ec0e15bbe91/resource/dd3b3932-b47b-443e-8c30-5eb8e4d91e2c/download/datapackage.json')
# resource = package.get_resource('servidores-2022-12')
# pd = resource.to_pandas()

# Using pandas
df = pd.read_csv('https://dados.mg.gov.br/dataset/98b58ea9-813e-4f50-8555-4ec0e15bbe91/resource/16920d4e-b88d-4994-8bc2-63ce8543fce6/download/servidores-2022-12.csv.gz',
				compression='gzip', 
				header=0, sep=';', 
				encoding='cp1252',
				)
new_df = df.query("descinst == 'FHEMIG FUND HOSPITALAR EST MG'")
print(f'Arquivo remuneração filtrado, sendo salvo em ~/Downloads/{today}_fhemig.xlsx')
new_df.to_excel(f'~/Downloads/{today}_fhemig.xlsx', encoding='utf8')