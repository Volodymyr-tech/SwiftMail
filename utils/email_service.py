from django.utils import timezone
from django.core.mail import send_mail

from config import settings
from mailing.models import MailingAttempt, Mail


class EmailSender:

    @staticmethod
    def send_mailing(mailing):
        recipients = mailing.client.all()
        subject = mailing.message.subject
        message = mailing.message.body
        from_email = settings.EMAIL_HOST_USER

        for recipient in recipients:
            try:
                # Отправка письма
                send_mail(
                    subject,
                    message,
                    from_email,
                    [recipient.email],
                    fail_silently=False,
                )
                # Фиксация успешной попытки
                MailingAttempt.objects.create(
                    mail=mailing,
                    status="successfully",
                    date_attempt=timezone.now(),
                    server_response="Newsletter was sent",
                    owner=mailing.owner,
                )

            except Exception as e:
                # Фиксация неудачной попытки
                MailingAttempt.objects.create(
                    mail=mailing,
                    status="not_successfully",
                    date_attempt=timezone.now(),
                    server_response=str(e),
                    owner=mailing.owner,
                )

        # Обновление статуса рассылки
        mailing.status = "Sent"
        mailing.save()
