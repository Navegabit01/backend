from rest_framework import serializers
from .models import Language, Translate, Translate_relation


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'code', 'siglas')
        read_only_fields = ('id',)


class TranslateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translate
        fields = ('id', 'trans_value', 'native_value', 'language_trans')
        read_only_fields = ('id',)


class Translate_relationSerializer(serializers.ModelSerializer):
  
      class Meta:
        model = Translate_relation
        fields = ('id','translate', 'menu_translate', 'card_translate')
        read_only_fields = ('id',)
