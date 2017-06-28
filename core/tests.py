from django.test import TestCase, Client
from django.contrib import auth


# Create your tests here.
from .models import Projeto, User, PropostaUser

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


# class PropostaUserCreate(CreateView):

# class PropostaProjetoCreate(CreateView):
# class UserPropostasList(ListView):
