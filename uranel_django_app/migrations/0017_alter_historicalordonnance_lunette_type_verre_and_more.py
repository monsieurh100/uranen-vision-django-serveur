# Generated by Django 4.2.14 on 2024-08-27 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uranel_django_app', '0016_stock_lunette'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalordonnance_lunette',
            name='type_verre',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ordonnance_lunette',
            name='type_verre',
            field=models.CharField(max_length=40),
        ),
    ]
