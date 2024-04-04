from django.db import models

class Time(models.Model):

    ESTADO_CHOICES = (
        ('SP', 'São Paulo'),
        ('RJ', 'Rio de Janeiro'),
        ('PI', 'Piauí'),
    )

    nome = models.CharField(max_length=120)
    estado = models.CharField(max_length=120, choices=ESTADO_CHOICES)
    cores = models.CharField(max_length=80)
    ano_de_fundacao = models.PositiveIntegerField(default=1970)
    tem_mundial = models.BooleanField(default=True)

    def __str__(self):
        return self.nome