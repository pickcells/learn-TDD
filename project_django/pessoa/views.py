from django.shortcuts import render
from django.http import JsonResponse
from pessoa.models import Pessoa
from django.views import View

# Create your views here.
class PessoaViews(View):
    def pessoa_list(request):
        obj = Pessoa.objects.all()
        # nova_pessoa = {
        #     "nome": "João",
        #     "idade": "20",
        # }
        # obj.create(**nova_pessoa).save()
        print(obj)
        return JsonResponse({"key":"value"})
