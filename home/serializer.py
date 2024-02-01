from rest_framework import serializers
from .models import MenuItem, MenuType


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('id', 'name', 'url', 'submenu', 'button',
                  'divider', 'icon', 'parent', 'type')
        read_only_fields = ('id',)


class MenuTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuType
        fields = ('id', 'type')
        read_only_fields = ('id',)
