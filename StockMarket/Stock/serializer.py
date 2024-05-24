from rest_framework import serializers

from Stock.models import Stock


class CreateStockSer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"

    def create(self, validated_data):
        return super().create(validated_data)


class GetStockSer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"

    def to_representation(self, instance):
        return super().to_representation(instance)
