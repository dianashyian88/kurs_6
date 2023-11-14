from django.db import models
from config.settings import AUTH_USER_MODEL


NULLABLE = {'null': True, 'blank': True}


class Message(models.Model):
    title_message = models.CharField(max_length=50, verbose_name='тема письма')
    body_message = models.TextField(verbose_name='текст письма')

    def __str__(self):
        return f'{self.title_message}'

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'
        ordering = ('id',)


class Distribution(models.Model):
    FREQUENCY_CHOICES = [
        ('once_day', '1 раз в день'),
        ('once_week', '1 раз в неделю (по понедельникам)'),
        ('once_month', '1 раз в месяц (в первый день месяца)'),
    ]
    STATUS_CHOICES = [
        ('C', 'Создана'),
        ('R', 'Идет рассылка писем'),
        ('F', 'Завершена'),
    ]
    name = models.CharField(max_length=50, verbose_name='наименование')
    start_datetime = models.DateTimeField(verbose_name='дата и время начала рассылки')
    end_datetime = models.DateTimeField(verbose_name='дата и время окончания рассылки')
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES, default='once_day',
                                 verbose_name='периодичность')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='C',
                              verbose_name='статус')
    message_id = models.ForeignKey(Message, on_delete=models.CASCADE,
                                   verbose_name='идентификатор письма для отправки', **NULLABLE)
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='пользователь', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('id',)


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО')
    description = models.TextField(verbose_name='комментарий')
    email = models.EmailField(verbose_name='почта')
    distribution_id = models.ForeignKey(Distribution, on_delete=models.CASCADE,
                                        verbose_name='идентификатор рассылки', **NULLABLE)
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='пользователь', **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ('id',)


class DistributionLogs(models.Model):
    STATUS_CHOICES = [
        ('C', 'Отклонена'),
        ('F', 'Завершена'),
    ]
    distribution_id = models.ForeignKey(Distribution, on_delete=models.CASCADE,
                                        verbose_name='идентификатор рассылки')
    start_datetime = models.DateTimeField(verbose_name='дата и время начала последней рассылки')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='статус')
    server_response = models.CharField(max_length=100, verbose_name='ответ почтового сервера')

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
        ordering = ('id',)
