from django.test import TestCase

# Create your tests here.
from models import Emprego

def criar_emprego():
    emprego = Emprego.objects.create(nome='Teste',
                                     descricao='Teste',
                                     empresa='Teste',
                                     area_atuacao='Teste',
                                     local_trabalho='Teste',
                                     quantidade_vagas=10,
                                     jornada_trabalho=8,
                                     salario=10.00,
                                     atribuicoes='Teste, teste etes',
                                     status=True)

    return emprego


#class EmpregoViewTest(TestCase):
