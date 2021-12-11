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

# E aqui mostramos que o modelo Author deve vir junto com os inlines: Books e Albums
# Isso vai fazer com que o registro de um autor sempre venha acompanhado do registro de Books e Albums
class AuthorAdmin(admin.ModelAdmin):
    inlines = [
        BookInline,
        AlbumInline,
    ]

# Essa é a forma padrão de registrar nossos modelos, dessa forma eles surgirão na nossa interface
admin.site.register(Cliente)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Books)
admin.site.register(Albums)


