# Generated by Django 4.2.14 on 2024-08-27 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uranel_django_app', '0021_remove_historicalvente_type_operation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock_autre',
            name='prix_unitaire',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
