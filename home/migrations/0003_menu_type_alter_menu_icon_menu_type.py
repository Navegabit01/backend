# Generated by Django 4.2.3 on 2023-07-19 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_menu_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('orientation', models.CharField(choices=[('horizontal', 'horizontal'), ('vertical', 'vertical')], default='horizontal', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='menu',
            name='icon',
            field=models.CharField(max_length=255),
        ),
        migrations.AddField(
            model_name='menu',
            name='type',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.menu_type'),
        ),
    ]
