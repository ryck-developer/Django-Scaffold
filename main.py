import argparse
from django.db import models


# Crie um parser de argumentos
parser = argparse.ArgumentParser()

# Adicione os argumentos necessários
parser.add_argument('--models', required=True, help='Nome do modelo para criar a view')
parser.add_argument('--atributos', nargs='+', required=True, help='Lista de atributos do modelo para incluir na view')

# Processa os argumentos
args = parser.parse_args()

# Pega o nome do modelo e a lista de atributos
model_name = args.models
attributes = args.atributos


for i in attributes:
    attr = i.split(':')
    if hasattr(models, attr[-1]):
        char_field = getattr(models, 'CharField')
        # char_field é o valor do atributo CharField em models
        print(char_field)
    else:
        print(f'O atributo [ {attr[0]} ] não possui um valor válido: {attr[-1]}')
        # models não tem um atributo chamado CharField


#print({model_name:attributes})


"""
python generate_view.py --models Funcionario --atributos nome salario_bruto horas_trabalhadas descontos impostos

"""
