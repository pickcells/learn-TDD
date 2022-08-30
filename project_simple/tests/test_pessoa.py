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
    
    def test_pessoa(self):
        self.assertEqual(self.pessoa.get_name, "")

if __name__ == '__main__':
    main(verbosity=2)