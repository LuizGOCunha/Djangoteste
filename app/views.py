from django.shortcuts import render
from app.models import Cliente, Author, Albums, Books
# Create your views here.
# Em views é onde o Django irá pegar os templates criados para dar forma à informação e dar forma junto aos models e
# e seus objetos que estão sendo guardados na database.

# Podemos fazer um index teste e retornar uma string diretamente através do HttpResponse


# A função render recebe o httprequest em seu primeiro argumento, retornando-o junto do arquivo a ser renderizado
def index(request):
    return render(request,"index.html")


def index2(request):
    return render(request,'index2.html')


def busca(request):
    return render(request, "search.html")