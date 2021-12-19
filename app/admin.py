from django.contrib import admin

# Register your models here.
from app.models import Cliente, Books, Author, Albums


# Uma forma de alterar a exibição do prompt da interface de adição de objeto do modelo Books
# Aqui ele vai surgir em formato Tabular (e Inline)
class BookInline(admin.TabularInline):
    model = Books


# Aqui ALbums vai surgir em formato Stacked (e Inline)
class AlbumInline(admin.StackedInline):
    model = Albums


# Essa classe vai informar ao admin como nosso objeto deve aparecer em sua interface. Vamos ver cada campo:
    # list_displayer: Quais atributos do nosso modelo vai representá-lo em sua fileira.
    # list_display_link: Quais atributos surgirão em formato de link.
    # list_filter: quais categorias vão surgir ao lado para serem selecionadas. (Deve ser tupla)
    # search_fields: Um campo de busca que irá procurar pelo nome do atributo citado. (Deve ser tupla)
class ClienteInLista(admin.ModelAdmin):
    list_display = ('id', 'nome', 'data', "pontuation")
    list_display_links = ('id', 'nome', 'data', "pontuation")
    list_filter = ('data',)
    search_fields = ('nome',)


class ArteInLista(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'publicacao')
    list_display_links = ('titulo', 'autor', 'publicacao')


# E aqui mostramos que o modelo Author deve vir junto com os inlines: Books e Albums
# Isso vai fazer com que o registro de um autor sempre venha acompanhado do registro de Books e Albums
# Alias, colocamos ele para herdar do clienteinlista poisnão podemos ter duas classes admin ao mesmo tempo
class AuthorAdmin(ClienteInLista):
    inlines = [
        BookInline,
        AlbumInline,
    ]


# Essa é a forma padrão de registrar nossos modelos, dessa forma eles surgirão na nossa interface
admin.site.register(Cliente, ClienteInLista)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Books, ArteInLista)
admin.site.register(Albums, ArteInLista)


