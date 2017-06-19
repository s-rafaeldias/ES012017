from django.test import TestCase

# Create your tests here.
from models import Freela


def teste_para_criacao_de_freelas():
    freela = Freela.objects.create(nome='Teste',
                                     descricao='Teste',
                                     area_atuacao='Teste',
                                     local_trabalho='Teste',
                                     jornada_trabalho=8,
                                     remuneracao=10.00,
                                     status=True)

    return freela

