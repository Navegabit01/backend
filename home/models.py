from django.db import models


class MenuType(models.Model):
    """Definition of type object"""
    type = models.CharField(max_length=100)
    create_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.type


class MenuItem(models.Model):
    """Definition of element object"""
    name = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True, default=None)
    submenu = models.BooleanField(default=False)
    divider = models.BooleanField(default=False)
    button = models.BooleanField(default=False)
    icon = models.ImageField(
        'image',
        upload_to='icons',
        null=True,
        blank=True,
        default=None
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    type = models.ForeignKey(
        "MenuType",
        on_delete=models.CASCADE
    )
    create_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
