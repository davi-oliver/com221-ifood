# Generated by Django 3.2.13 on 2022-07-04 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_bancario_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacomum',
            name='fechamentoConta',
            field=models.DateField(null=True),
        ),
    ]
