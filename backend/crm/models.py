from django.db import models

from backend.core.models import Endereço


class Cliente(Endereço):
    razao_social = models.CharField('Razão_Social', max_length=120, unique=True)
    cnpj = models.CharField('CNPJ', max_length=14,blank=True)

    class Meta:
        ordering = ('razao_social',)
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    def __str__(self):
        return f'{self.razao_social}'
    
