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
        
    def test_pessoa_name_is_string_type(self):
        self.assertEqual(type(self.pessoa.get_name), str)
        
    def test_pessoa_birth_year_is_not_int_type(self):
        self.assertNotEqual(type(self.pessoa.get_birth_year), int)

if __name__ == '__main__':
    main(verbosity=2)