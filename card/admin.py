from django.contrib import admin

from .models import Card

from .models import CardsType

admin.site.register(Card)

admin.site.register(CardsType)
