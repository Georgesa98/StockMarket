from rest_framework import serializers

from Stock.models import Stock
from User.models import User
from .exceptions import InsufficientStockQuantityException

from .models import Transaction, UserStock

Choices = (("BUY", "BUY"), ("SELL", "SELL"))


class CreateTransactionSer(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices=Choices)

    class Meta:
        model = Transaction
        fields = "__all__"

    def create(self, validated_data):
        if validated_data["type"] == "BUY":
            stock = Stock.objects.get(pk=validated_data["stock"].id)
            user = User.objects.get(pk=validated_data["user"].id)
            user.balance -= validated_data["amount"]
            user.save()
            stock.last_price += 0.1 / 100
            obj, created = UserStock.objects.update_or_create(
                user=validated_data["user"],
                stock=validated_data["stock"],
            )

            if created == False:
                obj.quantity += validated_data["quantity"]
                obj.save()
            else:
                obj.quantity = validated_data["quantity"]

            stock.save()

        elif validated_data["type"] == "SELL":
            user_stock = UserStock.objects.get(user=validated_data["user"])
            if user_stock.quantity >= validated_data["quantity"]:
                stock = Stock.objects.get(pk=validated_data["stock"].id)
                stock.last_price -= 0.05 / 100
                stock.save()
                user_stock.quantity -= validated_data["quantity"]
                user_stock.save()
                user = User.objects.get(validated_data["user"])
                user.balance -= validated_data["amount"]
                user.save()
            else:
                raise InsufficientStockQuantityException(
                    "Insufficient stock quantity to sell"
                )
        transaction = Transaction.objects.create(**validated_data)
        return transaction
