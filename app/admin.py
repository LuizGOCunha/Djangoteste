from django.contrib import admin

# Register your models here.
from app.models import Cliente, Books, Author

# Essa é a forma padrão de registrar nossos modelos, dessa forma eles surgirão na nossa interface (No nosso db? Não sei)
admin.site.register(Cliente)
admin.site.register(Books)
admin.site.register(Author)



