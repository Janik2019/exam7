# Generated by Django 2.2 on 2019-10-19 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20191019_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='question',
            field=models.CharField(max_length=300, verbose_name='Название Опроса'),
        ),
    ]
