from django.db import models

class Card(models.Model):
    name = models.CharField('ФИО', max_length=50)
    contact = models.CharField('Контактная информация', max_length=70)
    desk = models.TextField('Описание услуги')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'