from django.contrib import admin

# Register your models here.

from .models import Translate, Language, Translate_relation

admin.site.register(Translate)

admin.site.register(Language)

admin.site.register(Translate_relation)