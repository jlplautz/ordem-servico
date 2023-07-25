from django.db import models

from backend.crm.models import Cliente


class Servico(models.Model):
    titulo = models.CharField('Título', max_length=100)

    class Meta:
        ordering = ('titulo',)
        verbose_name = 'serviço'
        verbose_name_plural = 'serviços'

    def __str__(self):
        return f'{self.titulo}'
    

SITUACAO = {
    ('pe','Pendente'),
    ('ca','Cancelado'),
    ('ap','Aprovado'),
    ('an','Andamento'),
}


class OrdemServico(models.Model):
    situacao = models.CharField('Situação', max_length=2, choices=SITUACAO)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.SET_NULL,
        verbose_name = 'cliente',
        related_name = 'ordem_serviços',
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'ordem de serviço'
        verbose_name_plural = 'ordens de serviço'

    def __str__(self):
        return f'{self.pk}'


class OrdemServicoItem(models.Model):
    ordem_servico = models.ForeignKey(
        OrdemServico,
        on_delete=models.CASCADE,
        verbose_name = 'ordem de serviço',
        related_name = 'ordem_servico_itens',
    )
    servico = models.ForeignKey(
        Servico,
        on_delete=models.CASCADE,
        verbose_name = 'serviço',
        related_name = 'ordem_servico_item_servicos',
    )
    valor = models.DecimalField(
        'valor',
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
    )
    proxima_visita = models.DateTimeField(
        'Próxima Visita',
        null=True,
        blank=True,
    )


    class Meta:
        ordering = ('-pk',)
        verbose_name = 'item da ordem de serviço'
        verbose_name_plural = 'itens da ordem de serviço'

    def __str__(self):
        return f'{self.pk}'