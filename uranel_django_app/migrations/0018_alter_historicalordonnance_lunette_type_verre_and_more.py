# Generated by Django 4.2.14 on 2024-08-27 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uranel_django_app', '0017_alter_historicalordonnance_lunette_type_verre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalordonnance_lunette',
            name='type_verre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ordonnance_lunette',
            name='type_verre',
            field=models.CharField(max_length=100),
        ),
    ]
