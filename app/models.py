from django.db import models

# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length = 100)
    data = models.DateField(blank=True,null=True)
    pontuation = models.IntegerField(blank=True,null=True)
    habilitado = models.BooleanField(blank=True,null=True)
    obs = models.TextField(blank=True,null=True)

    # Esse método tem como objetivo mudar a apresentação de cada objeto deste modelo.
    # Aqui, escolhemos representá-lo pelo atributo 'nome'
    def __str__(self):
        return self.nome


class Books(models.Model):
    titulo = models.CharField(max_length=200)
    publicacao = models.DateField(blank=False)
    edicao = models.CharField(max_length=50)
    paginas = models.IntegerField(blank=False)
    sinopse = models.TextField(blank=True, null=True)

    # Essa classe tem como objetivo mudar a forma como o Django se refere à nosso modelo em sua interface
    class Meta:
        verbose_name_plural = "Livros"

    def __str__(self):
        return self.titulo


class Author(Cliente):
    # Aqui ligamos o modelo author a um modelo books através de uma ForeignKey.
    # Isto é, ligamos um autor ao livro de sua autoria
    books = models.ForeignKey(Books, on_delete=models.PROTECT)
    pseudonimo = models.CharField(max_length=100, blank=True, null=True)
    premiado = models.BooleanField(blank=False)
    parceiro = models.BooleanField(blank=False)

    class Meta:
        verbose_name_plural = "Autores"

