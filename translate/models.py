from django.db import models


# Create your models here.
class Language(models.Model):
    """Definition of language object"""
    code = models.CharField(
        max_length=255, default="", blank=False, null=False)
    siglas = models.CharField(
        max_length=255, default="", blank=False, null=False)

    def __str__(self):
        return self.siglas


class Translate(models.Model):
    """Definition of translate object"""
    trans_value = models.TextField(
        max_length=2000, default="", blank=False, null=False)
    native_value = models.CharField(
        max_length=2000, default="", blank=False, null=False)
    language_trans = models.ForeignKey(
        'Language',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default=""
    )

    def __str__(self):
        return self.trans_value


class Translate_relation(models.Model):
    """Definition of translate relation object"""
    translate = models.ForeignKey(
        'Translate',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=""
    )
    menu_translate = models.ForeignKey(
        'home.MenuItem',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=""
    )
    card_translate = models.ForeignKey(
        'card.Card',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=""
    )
