from django.test import TestCase
from pessoa.models import Pessoa

class PessoaTestCase(TestCase):
    def setUp(self):
        Pessoa.objects.create(nome="Jeremias", idade=20)
        Pessoa.objects.create(nome="Maria", idade=25)
        Pessoa.objects.create(nome="José", idade=30)
    
    def test_pessoa_nome(self):
        pessoa = Pessoa.objects.get(nome="Maria")
        self.assertEqual(pessoa.nome, "maria")