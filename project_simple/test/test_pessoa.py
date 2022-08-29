try:
    import sys
    import os
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), '..'
            )
        )
    )
except:
    raise
from unittest import TestCase, main
from classes.pessoa import Pessoa

class TestePessoa(TestCase):
    def setUp(self):
        self.pessoa = Pessoa()
    
    def test_pessoa_init(self):
        self.assertEqual(self.pessoa.get_name, "")
        self.assertEqual(self.pessoa.get_birth_year, 0)
        self.assertEqual(self.pessoa.get_weight, 0.0)
    
    


main(verbosity=2)