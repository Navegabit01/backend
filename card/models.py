from django.db import models


class Card(models.Model):
    """Definition of card object"""
    title = models.CharField(
        max_length=1024,
        default="",
        blank=False,
        null=False
    )
    text = models.TextField(max_length=4096, default="", blank=False)
    url = models.URLField()
    order = models.IntegerField(default=0, )
    type = models.ForeignKey(
        'CardsType',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default=""
    )
    image = models.ImageField(
        'image',
        upload_to='photos',
        blank=False,
        null=False,
        default=None
    )
    active = models.BooleanField('Active', default=True)

    def __str__(self):
        return self.title


class CardsType(models.Model):
    """Definition of card type object"""
    type = models.CharField(max_length=150)
    active = models.BooleanField('Active', default=True)

    def __str__(self):
        return self.type

# Create your models here.
