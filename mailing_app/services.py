from datetime import datetime, timedelta

from django.conf import settings
from django.utils import timezone
from apscheduler.schedulers.background import BackgroundScheduler

from config.settings import EMAIL_HOST_USER
from .models import Mailing, MailingTrying, Client
from django.core.mail import send_mail


def check_and_send_mailings():
    mailings = Mailing.objects.filter(status=Mailing.Status.CREATED, next_mailing__lte=timezone.now())

    for mailing in mailings:
        mailing.status = Mailing.Status.RUNNING
        mailing.save()

        try:

            clients = mailing.clients.all()
            mail_subject = mailing.mail.topic
            mail_content = mailing.mail.content

            for client in clients:
                send_mail(
                    mail_subject,
                    mail_content,
                    settings.EMAIL_HOST_USER,
                    [client.email],
                    fail_silently=False,
                )

            MailingTrying.objects.create(
                last_mailing=timezone.now(),
                status_trying='SC',
                server_response="Письма отправлены",
                mailing=mailing
                )

            mailing.set_next_mailing_after_send()

            mailing.status = Mailing.Status.CREATED
            mailing.save()

            print(f"Рассылка для {mailing} была успешно отправлена.")

        except Exception as e:

            MailingTrying.objects.create(
                last_mailing=timezone.now(),
                status_trying='failed',
                server_response=str(e),
                mailing=mailing
            )

            mailing.status = 'failed'
            mailing.save()

            print(f"Рассылка для {mailing} не отправлена. Произошла ошибка. ")

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_and_send_mailings, 'interval', minutes=1)
    scheduler.start()

