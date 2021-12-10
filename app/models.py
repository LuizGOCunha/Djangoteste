from django.db import models

# Create your models here.


# Isso é um modelo, nada mais que uma classe de objeto que encontraremos em nosso site, e que armazenaremos em nossa db.
class Cliente(models.Model):
# Abaixo temos os tipos mais comuns de dados que serão utilizados, e também formas comuns de categoricá-los.
# Além disso, temos argumentos que nos ajudam a especificar limites e permissões para esses dados, como:
    # null = dita que ao receber uma caixa vazia, deve retornar valor nulo, ao invés de uma string vazia.
    # blank = dita se a caixa aceita uma caixa vazia.
    # max_length = dita o maximo de caracteres.
    # choices = dita um número de escolhas através de um objeto tuple, cada valor dentro do objeto tuple sendo duplo,
    # o motivo sendo que o primeiro será o valor guardado na db, o segundo será mostrado na interface. Exemplo:
        # cho_tuple = (('P', 'Pequeno'), ('M', 'Médio'), ('G', 'Grande')); models.Charfield(choices=cho_tuple)
    # default = Valor padrão para esta caixa. Pode ser um valor ou um objeto a ser chamado (o que isso significa?)
    # verbose_name = Dita como o nome da coluna de informação deve surgir na interface. (primeiro argumento)
    # primary_key = Boolean, se verdadeiro será a PK deste modelo (irá identificá-lo. Obrigatório e único!)
    # unique = Boolean, se verdadeiro diz que os valores nessa caixa não devem se repetir entre os objetos.
    # Você pode adicionar uma primary key assim, mas saiba que o Django já faz isso automaticamente:
        # id = models.BigAutoField(primary_key=True)
    nome = models.CharField('nome completo',max_length = 100) # Caixa de string pequena
    data = models.DateField(blank=True,null=True) # Caixa de data
    pontuation = models.IntegerField('pontuação',blank=True,null=True) # Caixa numérica
    habilitado = models.BooleanField('habitação',blank=True,null=True, choices=( ('s', 'sim'), ('n', 'não') )) # Caixa de valor binário (verdadeiro ou falso)
    obs = models.TextField('observação',blank=True,null=True) # Caixa de texto grande (parágrafo)

    # Esse método tem como objetivo mudar a apresentação de cada objeto deste modelo.
    # Aqui, escolhemos representá-lo pelo atributo 'nome'
    def __str__(self):
        return self.nome


class Books(models.Model):
    titulo = models.CharField('título',max_length=200)
    publicacao = models.DateField('publicação',blank=False) # O valor padrão de blank já é True, mas reforcei aqui.
    edicao = models.CharField('edição', max_length=50)
    paginas = models.IntegerField('quantidade de páginas',blank=False)
    sinopse = models.TextField('sinopse',blank=True, null=True)

    # Essa classe tem como objetivo mudar a forma como o Django se refere à nosso modelo (em plural) em sua interface
    class Meta:
        verbose_name_plural = "Livros"

    def __str__(self):
        return self.titulo


class Albums(models.Model):
    titulo = models.CharField('título',max_length=100)
    publicacao = models.DateField('publicação',blank=False)
    duracao = models.IntegerField('duração')


class Author(Cliente):
    # Aqui ligamos o modelo author a um modelo books através de uma ForeignKey.
    # Isto é, ligamos um autor ao livro de sua autoria
    books = models.ForeignKey(Books, on_delete=models.CASCADE) # on_delete: ação a ser feita quando o model for deletado
    albums = models.ForeignKey(Albums, on_delete=models.CASCADE)
    # PROTECT: Não deleta o modelo até que todos os objetos dependentes sejam deletados.
    # CASCADE: Ao deletar o objeto, todos os seus dependentes também são deletados
    # RESTRICT: Similar ao PROTECT, mas se aproximando à ação de mesmo nome em SQL
    # SET_NULL: Ao deletar o objeto, mantém o espaço e todos os objetos dependentes, mas reduz o valor a nulo.
    # SET_DEFAULT: Seta um valor padrão.
    # SET (...): Estabelecer um valor a ser adotado ao deletar o objeto.
    # DO_NOTHING: Autoexplicativo, e também uma péssima ideia em geral.
    pseudonimo = models.CharField(max_length=100, blank=True, null=True)
    premiado = models.BooleanField(blank=False,choices=( ('s', 'sim'), ('n', 'não') ))
    parceiro = models.BooleanField(blank=False, choices=( ('s', 'sim'), ('n', 'não') ))

    class Meta:
        verbose_name_plural = "Autores"

