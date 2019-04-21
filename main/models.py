from django.db import models


class ServicesTypes(models.Model):
    service_type = models.CharField('Тип услуги', max_length=128, unique=True)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Тип услуги'
        verbose_name_plural = 'Типы услуг'


class ServicesKinds(models.Model):
    service_type = models.ForeignKey(ServicesTypes, on_delete=models.CASCADE,
                                     verbose_name='Тип услуги', default='none')
    service_kind = models.CharField('Вид услуги', max_length=128, unique=True)

    def __str__(self):
        return f'{self.service_type}: {self.service_kind}'

    class Meta:
        verbose_name = 'Вид услуги'
        verbose_name_plural = 'Виды услуг'


class Applictions(models.Model):
    client_name = models.CharField('Имя клиента', max_length=40)
    phone = models.CharField('Номер телефона', max_length=20)
    email = models.EmailField('E-mail', null=True)
    service_kind = models.ForeignKey(ServicesKinds, on_delete=models.CASCADE,
                                     verbose_name='Услуга', default='none')
    message = models.TextField('Сообщение')
    treatment_data = models.DateField('Дата обращения', auto_now_add=True)
    is_close = models.BooleanField('Закрыта ли заявка')

    def __str__(self):
        return f'{self.client_name}\n{self.service_kind}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
