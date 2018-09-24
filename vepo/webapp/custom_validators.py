from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def check_kwh(value):

    value_list = [i for i in value]
    totalCheck = []

    for values in value_list:
        try:
            validInput = int(values)
            totalCheck.append('int')
        except:
            totalCheck.append('str')

    if 'str' in totalCheck:
        raise ValidationError("Por favor, inserir somente números para o seu consumo")
    else:
        return value


def check_cep(value):
    totalCheck = []

    if len(value) != 9:
        raise ValidationError("Por favor, entre o seu CEP no formato 12345-678")
    else:
        try:
            for i in value.split('-')[0]:
                try:
                    validInput = int(i)
                    totalCheck.append('int')
                except:
                    totalCheck.append('str')

            for i in value.split('-')[1]:
                try:
                    validInput = int(i)
                    totalCheck.append('int')
                except:
                    totalCheck.append('str')
        except:
            raise ValidationError("Por favor, entre o seu CEP no formato 12345-678")

    # print(totalCheck)

    if 'str' in totalCheck:
        raise ValidationError("Por favor, entre o seu CEP no formato 12345-678")
    else:
        return value
