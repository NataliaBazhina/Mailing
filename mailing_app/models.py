from datetime import timedelta
from django.utils import timezone
from django.db import models
from clients_app.models import Client



class Mail(models.Model):
    topic = models.CharField(max_length=35, verbose_name='тема письма')
    content = models.TextField(verbose_name='тело письма')

    def __str__(self):
        return self.topic


class Mailing(models.Model):
    class Status(models.TextChoices):
        CREATED = "CR", "Создана"
        RUNNING = "RN", "Запущена"

    class Frequency(models.TextChoices):
        DAILY = 'DY', "Раз в день"
        WEEKLY = "WE", "Раз в неделю"
        MONTHLY = 'MN', "Раз в месяц"

    first_mailing = models.DateTimeField(verbose_name='первая рассылка', null=True, blank=True)

    frequency = models.CharField(
        max_length=2,
        choices=Frequency.choices,
        default=Frequency.DAILY,
        verbose_name="Периодичность",
    )

    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.CREATED,
        verbose_name="статус",
    )

    clients = models.ManyToManyField(Client)
    mail = models.ForeignKey(Mail, on_delete=models.CASCADE)

    next_mailing = models.DateTimeField(null=False, blank=True, default=timezone.now, verbose_name='Следующая рассылка')

    def save(self, *args, **kwargs):
        if not self.next_mailing and self.first_mailing:
            self.next_mailing = self.first_mailing

        super().save(*args, **kwargs)

    def set_next_mailing_after_send(self):
        if self.frequency == self.Frequency.DAILY:
            self.next_mailing = self.next_mailing + timedelta(days=1)
        elif self.frequency == self.Frequency.WEEKLY:
            self.next_mailing = self.next_mailing + timedelta(weeks=1)
        elif self.frequency == self.Frequency.MONTHLY:
            self.next_mailing = self.next_mailing + timedelta(weeks=4)


class MailingTrying(models.Model):
    class Status(models.TextChoices):
        SUCCESS = "SC", "Успешно"
        FAILED = "FL", "Неуспешно"

    last_mailing = models.DateTimeField(verbose_name='последняя рассылка')
    status_trying = models.CharField(
        max_length=2,
        choices=Status.choices,
        verbose_name="статус попытки")
    server_response = models.CharField(max_length=1000)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, null=True, blank=True)