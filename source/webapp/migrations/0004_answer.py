# Generated by Django 2.2 on 2019-10-19 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20191019_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания ответа')),
                ('choice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='webapp.Choice', verbose_name='Ответы')),
                ('poll', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='webapp.Poll', verbose_name='Ответы')),
            ],
        ),
    ]
