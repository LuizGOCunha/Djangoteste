from django.contrib import admin

# Register your models here.
from app.models import Cliente, Books, Author

admin.site.register(Cliente)
admin.site.register(Books)
admin.site.register(Author)



