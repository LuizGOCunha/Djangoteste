from django.db import models

# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length = 100)
    data = models.DateField(blank=True,null=True)
    pontuation = models.IntegerField(blank=True,null=True)
    habilitado = models.BooleanField(blank=True,null=True)
    obs = models.TextField(blank=True,null=True)