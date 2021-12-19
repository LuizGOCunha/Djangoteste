from django.urls import path
from . import views

# Este é um arquivo que não vem junto da aplicação base Django, ele deve ser feito pelo usuário
# Aqui é onde colocaremos subdomínios da aplicação "app", e então apontamos o urls.py do root para que ele possa checar
# os endereços aqui também.
# Basicamente: o urls.py root é um fork dos caminhos de onde é possível ir em um site, o urls do app é um nested fork.


# Após encontrar o caminho a ser carregado no primeiro urls, o Django busca a variavel "urlpatterns", como se vê abaixo.
# Essa variável deve ser uma lista contendo várias instâncias da função path() ou re_path()
# Ele vai checar todos os urls, e parar naquele que se assemelha(primeiro arg) com o request e executá-lo (segundo arg)
# Se o nome da url for uma string vazia, então será levado em consideração o url base do aplicativo
# Sempre bom nomear seus paths com a variavel 'name', para fins de referencia
urlpatterns = [
    path('', views.index, name='index'),
    path('busca/', views.busca, name = 'busca'),
]
