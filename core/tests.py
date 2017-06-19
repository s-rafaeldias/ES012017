from django.test import TestCase

# Create your tests here.
from models import Projeto


def teste_para_criacao_de_projeto():
    projeto = Projeto.objects.create(nome='Teste',
                                     descricao='Teste',
                                     area_atuacao='Teste',
                                     local_trabalho='Teste',
                                     duracao=8,
                                     remuneracao=10.00,
                                     status=True)

    return projeto
