from django.db import models
# Create your models here.
class Unidade (models.Model):
    nome = models.CharField(max_length=120)
    endereco = models.CharField (max_length=200, blanck=True)

    def __str__(self):
        return self.nome
    
class Sala (models.Model):
    Unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, related_name="salas")
    nome = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.Unidade.nome} - {self.nome}"
    
class Status (models.Model):
    nome = models.CharField (max_length=100)
    descricao = models.TextField (blank=True)

    def __str__(self):
        return self.nome
    
class Bem (models.Model):
    nome = models.CharField (max_length=200)
    tombo = models.CharField (max_length=50, unique=True)
    unidade = models.ForeignKey (Unidade, on_delete=models.PROTECT, related_name="bens")
    sala = models.ForeignKey (Sala, on_delete=models.SET_NULL, null=True, blanck=True)
    Status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)

    criado_em = models.DataTimeField (auto_now_add=True)
    atualizado_em = models.DataTimeField (auto_now=True)

    def __str__(self):
        return f"{self.nome} ({self.tombo})"