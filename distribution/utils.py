from distribution.models import Distribution, DistributionLogs
from django.utils import timezone
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
import datetime
from smtplib import SMTPException


def send_and_log(obj: Distribution):
    for obj_email in obj.emails.filter(owner=obj.owner):
        try:
            send_mail(
                subject=obj.message_id.title_message,
                message=obj.message_id.body_message,
                from_email=EMAIL_HOST_USER,
                recipient_list=[obj_email.email],
                fail_silently=False,
            )
            now = timezone.make_aware(datetime.datetime.now(), timezone.get_current_timezone())
            DistributionLogs.objects.create(
                start_datetime=now,
                distribution_id=obj,
                mail=obj_email.email,
                owner=obj.owner,
                server_response='Mail_sent',
                status='F'
            )
        except SMTPException as error:
            DistributionLogs.objects.create(
                start_datetime=now,
                distribution_id=obj,
                mail=obj_email.email,
                owner=obj.owner,
                server_response=error,
                status='C'
            )

def send_email_for_distribution():
    distribution_list = Distribution.objects.all()
    for obj in distribution_list:
        if obj.is_active:
            now = datetime.datetime.now()
            now = timezone.make_aware(now, timezone.get_current_timezone())
            if obj.status == 'C':
                if obj.start_datetime <= now:
                    if obj.end_datetime > now:
                        obj.status = 'R'
                        obj.save()
                    else:
                        obj.status = 'F'
                        obj.save()
            elif obj.status == 'R':
                if obj.end_datetime <= now:
                    obj.status = 'F'
                    obj.save()
                else:
                    if obj.last_datetime is None:
                        send_and_log(obj)
                        obj.last_datetime = now
                        obj.save()
                    else:
                        time_delta = (now - obj.last_datetime).days
                        if obj.frequency == 'once_day' and time_delta >= 1:
                            send_and_log(obj)
                            obj.last_datetime = now
                            obj.save()
                        elif obj.frequency == 'once_week' and time_delta >= 7:
                            send_and_log(obj)
                            obj.last_datetime = now
                            obj.save()
                        elif obj.frequency == 'once_month' and time_delta >= 30:
                            send_and_log(obj)
                            obj.last_datetime = now
                            obj.save()
