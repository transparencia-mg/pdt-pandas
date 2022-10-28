# Extraindo dados Portal Dados Abertos com Python Pandas

Este repositório mostra casos de uso de leitura de dados disponíveis no [Portal de Dados Abertos do Estado de Minas Gerais](https://dados.mg.gov.br) via biblioteca [Python Pandas](https://pandas.pydata.org/).
Os exemplos aqui propostos são apenas demonstrações simplificadas de como realizar esta leitura, cabendo ao usuário final montar suas tabelas  de acordo com cada necessidade.

Para realizar o setup do projeto localmente necessário ter [Python](https://www.python.org/downloads/) devidamente instalado na máquina.

## Setup Linux

```
# Criação Ambiente Virtual Python
python3 -m venv venv

# Ativação Ambiente Virtual Python
source venv/bin/activate

# Instalação Pacotes Necessários
pip install -r requirements.txt
```

## Setup Windows

```
# Criação Ambiente Virtual Python
python -m venv venv

# Ativação Ambiente Virtual Python
source venv/Scripts/activate

# Instalação Pacotes Necessários
pip install -r requirements.txt
```
## Visualização Exemplos

- [Compras e Contratos](https://dados.mg.gov.br/dataset/compras_contratos) executar o comando `python compras_contratos/main.py` na raiz do repositório.


