from django.test import TestCase, Client
from django.contrib import auth


# Create your tests here.
from .models import Projeto, User, PropostaUser, Projeto, PropostaProjeto

class CoreViewsTestCase(TestCase):

    def test_proposta_user_create(self):
        user = User.objects.get(pk=1)
        client = Client()
        client.login(username=user.username, password='Br@197795')

        # Teste de resposta 200
        resp = client.post('/propostaUser/2', {'dsc_proposta': 'Teste True'}, follow=True)
        self.assertEqual(resp.status_code, 200)

        # Teste para garantir que inseriu uma proposta
        prop = PropostaUser.objects.count()
        self.assertEqual(prop, 1)

        # Teste para garantir as informações corretas da proposta
        prop2 = PropostaUser.objects.get(dsc_proposta='Teste True')
        self.assertEqual(prop2.from_user_id, 1)
        self.assertEqual(prop2.to_user_id, 2)

    def test_proposta_projeto_create(self):

        Projeto.objects.create( nome='ProjetoTeste',
                                descricao='Dsc Projeto',
                                local_trabalho='Local Trabalho Projeto',
                                duracao=10,
                                remuneracao=1000,
                                status=True,
                                user=User.objects.get(pk=1))

        user = User.objects.get(pk=1)
        client = Client()
        client.login(username=user.username, password='Br@197795')

        url = '/newPropostaProjeto/%d' % Projeto.objects.get(nome='ProjetoTeste').id

        resp = client.post(url, { 'oferta': 100,
                                  'tempo': 100,
                                  'infos': 'Testesss'}, follow=True)

        self.assertEqual(resp.status_code, 200)

        prop3 = PropostaProjeto.objects.count()
        self.assertEqual(prop3, 1)
