from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Em views é onde o Django irá pegar os templates criados para dar forma à informação e dar forma junto aos models e
# e seus objetos que estão sendo guardados na database.


# Podemos fazer um index teste e retornar uma string diretamente através do HttpResponse
def index(request):
    return HttpResponse("Isso é um teste")