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
    # on_delete = ação a ser feita quando o model for deletado
    # primary_key = Boolean, se verdadeiro será a PK deste modelo (irá identificá-lo. Obrigatório e único!)
    # unique = Boolean, se verdadeiro diz que os valores nessa caixa não devem se repetir entre os objetos.
    # Você pode adicionar uma primary key assim, mas saiba que o Django já faz isso automaticamente:
        # id = models.BigAutoField(primary_key=True)
    nome = models.CharField('nome completo',max_length = 100) # Caixa de string pequena
    data = models.DateField(blank=True,null=True) # Caixa de data
    pontuation = models.IntegerField('pontuação',blank=True,null=True) # Caixa numérica
    # Caixa de valor binário (verdadeiro ou falso)
    habilitado = models.BooleanField('habitação',blank=True,null=True, choices=( (True, 'sim'), (False, 'não') ))
    obs = models.TextField('observação',blank=True,null=True) # Caixa de texto grande (parágrafo)
    # Essa é uma dificuldade que eu passei muito tempo tendo, como fazer um relacionamento de amizade entre usuarios?
    # Claramente se trata de um relacionamento many to many, mas eu não sabia como se referencia a si mesmo em Django
    # E aqui está resolvido, se usa self, assim como em python, mas se coloca em string.
    amigos = models.ManyToManyField("self",blank=True,null=True)

    # Esse método tem como objetivo mudar a apresentação de cada objeto deste modelo.
    # Aqui, escolhemos representá-lo pelo atributo 'nome'
    def __str__(self):
        return self.nome


class Author(Cliente):
    pseudonimo = models.CharField(max_length=100, blank=True, null=True)
    premiado = models.BooleanField(blank=False, choices=((True, 'sim'), (False, 'não')))
    parceiro = models.BooleanField(blank=False, choices=((True, 'sim'), (False, 'não')))

    class Meta:
        verbose_name_plural = "Autores"

    def __str__(self):
        return self.pseudonimo


class Books(models.Model):
    titulo = models.CharField('título',max_length=200)
    # Aqui ligamos o modelo books ao modelo autor através de uma ForeignKey. Criando uma relação many-to-one
    # Isto é, ligamos um ou mais livros ao seu autor. Mas existem outro tipo: Many to many
    # Many to many: relação de amigos em uma rede social.
    # Também é possível ver o argumento "on_delete", que diz o que fazer no caso de objetos dependentes serem apagados.
    # Abaixo temos todas as opções:
    # PROTECT: Não deleta o modelo até que todos os objetos dependentes sejam deletados.
    # CASCADE: Ao deletar o objeto, todos os seus dependentes também são deletados
    # RESTRICT: Similar ao PROTECT, mas se aproximando à ação de mesmo nome em SQL
    # SET_NULL: Ao deletar o objeto, mantém o espaço e todos os objetos dependentes, mas reduz o valor a nulo.
    # SET_DEFAULT: Seta um valor padrão.
    # SET (...): Estabelecer um valor a ser adotado ao deletar o objeto.
    # DO_NOTHING: Autoexplicativo, e também uma péssima ideia em geral.
    autor = models.ForeignKey(Author,on_delete=models.CASCADE,blank=True,null=True)
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
    autor = models.ForeignKey(Author,on_delete=models.CASCADE,blank=True,null=True)
    publicacao = models.DateField('publicação',blank=False)
    duracao = models.IntegerField('duração')

    class Meta:
        verbose_name_plural = "Albums"

    def __str__(self):
        return self.titulo


# Aqui eu já posso logar na interface localhost/admin e adicionar objetos por lá.
# Mas existem outras maneiras de fazer isso.
# Python console: Vá até o terminal e digite:
# $ python3 manage.py shell
# Em seguida importe a biblioteca 'os':
# >>> import os
# Então define a variavel de ambiente no seu settings (?)
# >>> os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_model.settings')
# Então importe o django
# >>> import django
# Então configura o django com os settings especificados
# >>> django.setup()
# Agora, é preciso importar o model oque você quer utilizar
# >>> from app.models import Cliente
# A partir daí tem duas maneiras de se criar um objeto e salvá-lo na database:
# instanciando e salvando:
# >>> joao = Cliente(nome = 'João', data ='1999-09-09',pontuation= 89,habilitado= True, obs='observado')
# >>> joao.save()
# Ou podemos fazer tudo em uma só linha:
# pedro = Cliente.objects.create(nome='Pedro',data='1985-04-18',pontuation=14,habilitado=False,obs='observei')

# É possível fazer uma função de Query ao misturar funcionalidades Django com uma simples Lambda function:
# >>> listar = lambda x: Cliente.objects.filter(id=x)
# >>> listar(1)
# Retorna: <QuerySet [<Cliente: Luiz>]>
# ou
# >>> clientegrep = lambda model,string: model.objects.filter(nome__contains=string)
# >>> clientegrep(Cliente, "ui")
# Retorna: <QuerySet [<Cliente: Luiz>, <Cliente: Luiz Gustavo Oliveira da Cunha>]>
# Assim podemos buscar objetos através da command line, sem precisar rodar o servidor nem acessar diretamente o db
