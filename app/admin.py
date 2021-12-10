from django.contrib import admin

# Register your models here.
from app.models import Cliente, Books, Author, Albums


class BookInline(admin.TabularInline):
    model = Books


class AlbumInline(admin.StackedInline):
    model = Albums


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


