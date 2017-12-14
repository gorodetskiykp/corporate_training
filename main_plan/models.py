from django.db import models


class TrainingType(models.Model):
    order_number = models.PositiveSmallIntegerField('Порядковый номер')
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        verbose_name='Родительская категория',
        blank=True,
        null=True)
    short_name = models.CharField('Сокращенное название', max_length=30, unique=True)
    full_name = models.CharField('Полное название', max_length=100, unique=True)
    training_of_managers = models.BooleanField('Обучение руководителей и специалистов', default=True)

    class Meta:
        ordering = ['order_number']
        verbose_name = 'Вид обучения'
        verbose_name_plural = 'Виды обучения'


class Plan(models.Model):
    training_type = models.ForeignKey(
        TrainingType,
        on_delete=models.SET_NULL,
        verbose_name='Тип обучения',
        blank=True,
        null=True)

    class Meta:
        ordering = ['training_type']
        verbose_name = 'План обучения'
        verbose_name_plural = 'Планы обучения'