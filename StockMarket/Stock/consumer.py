import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from Stock.models import Stock
from Stock.serializer import GetStockSer
from asgiref.sync import sync_to_async


@sync_to_async
def get_live_data():
    stocks = Stock.objects.all()
    return stocks


@sync_to_async
def serialize_data(data):
    serializer = GetStockSer(data, many=True)
    stock_data = serializer.data
    data_json = json.dumps(stock_data)
    return data_json


class StockConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()
        self.data_task = asyncio.create_task(self.handle_data())

    async def disconnect(self, close_code):
        self.data_task.cancel()

    async def handle_data(self):
        while True:
            stocks = await get_live_data()
            data = await serialize_data(stocks)
            await self.send(text_data=data)
            await asyncio.sleep(1)

    def receive(self, text_data):
        pass
