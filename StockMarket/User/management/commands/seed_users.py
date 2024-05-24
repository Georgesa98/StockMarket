from django.core.management.base import BaseCommand

from Stock.models import Stock
from User.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            for i in range(100):
                User.objects.create(
                    username=i, password="fakeuser", balance=100000, fullname=i
                )
            return "Done.."
        except Exception as e:
            return str(e)
