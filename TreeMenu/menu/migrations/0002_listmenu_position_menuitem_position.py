# Generated by Django 4.2 on 2023-05-01 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listmenu',
            name='position',
            field=models.IntegerField(default=1, verbose_name='Позиция'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='position',
            field=models.IntegerField(default=1, verbose_name='Позиция'),
        ),
    ]