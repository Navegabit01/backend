# Generated by Django 4.2.3 on 2023-07-18 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='icon',
            field=models.CharField(max_length=150),
        ),
    ]
