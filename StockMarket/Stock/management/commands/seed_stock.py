from django.core.management.base import BaseCommand

from Stock.models import Stock


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            Stock.objects.create(symbol="AAPL", co_name="Apple", last_price=153.22)
            Stock.objects.create(symbol="MSFT", co_name="Microsoft", last_price=305.15)
            Stock.objects.create(symbol="AMZN", co_name="Amazon", last_price=3425.00)
            Stock.objects.create(symbol="TSLA", co_name="Tesla", last_price=785.00)
            Stock.objects.create(
                symbol="GOOG", co_name="Alphabet Inc.", last_price=2527.44
            )
            Stock.objects.create(
                symbol="BAC", co_name="Bank Of America", last_price=42.22
            )
            return "Done.."
        except Exception as e:
            return str(e)
