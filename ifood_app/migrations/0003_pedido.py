# Generated by Django 4.0.6 on 2022-07-24 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ifood_app', '0002_endereco'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metodoPagamento', models.CharField(max_length=100)),
            ],
        ),
    ]
