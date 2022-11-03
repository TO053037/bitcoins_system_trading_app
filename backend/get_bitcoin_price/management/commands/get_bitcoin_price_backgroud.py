import time

from django.core.management.base import BaseCommand
from get_bitcoin_price.models import BitcoinPrice
import pybitflyer


class Command(BaseCommand):
    def handle(self, *args, **options):
        while True:
            response = pybitflyer.API().ticker(product_code='BTC_JPY')
            for k, v in response.items():
                print(k, v)
            BitcoinPrice.objects.create(
                state=response['state'],
                timestamp=response['timestamp'],
                tick_id=response['tick_id'],
                best_bid=response['best_bid'],
                best_ask=response['best_ask'],
                best_bid_size=response['best_bid_size'],
                best_ask_size=response['best_ask_size'],
                total_bid_depth=response['total_bid_depth'],
                total_ask_depth=response['total_ask_depth'],
                market_bid_size=response['market_bid_size'],
                market_ask_size=response['market_ask_size'],
                ltp=response['ltp'],
                volume=response['volume'],
                volume_by_product=response['volume_by_product'],
            )
            time.sleep(10)
