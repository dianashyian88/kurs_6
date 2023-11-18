from django.core.management.base import BaseCommand
from distribution.utils import send_email_for_distribution


class Command(BaseCommand):

    def handle(self, *args, **options):
        send_email_for_distribution()
