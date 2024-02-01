from rest_framework import serializers
from .models import Card, CardsType


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'title', 'text', 'active', 'url', 'order', 'image', 'type')
        read_only_fields = ('id',)


class CardTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardsType
        fields = ('id', 'type')
        read_only_fields = ('id',)
