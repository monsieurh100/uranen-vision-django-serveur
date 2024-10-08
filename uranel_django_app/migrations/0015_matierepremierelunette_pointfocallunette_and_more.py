# Generated by Django 4.2.14 on 2024-08-25 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uranel_django_app', '0014_historicalvente_total_vente_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatierePremiereLunette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MatierePremiereLunette', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'MatierePremiereLunettes',
                'verbose_name_plural': 'MatièrePremiereLunette',
            },
        ),
        migrations.CreateModel(
            name='PointFocalLunette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PointFocalLunette', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'PointFocalLunettes',
                'verbose_name_plural': 'PointFocalLunette',
            },
        ),
        migrations.CreateModel(
            name='TeinteLunette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TeinteLunette', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'TeinteLunettes',
                'verbose_name_plural': 'TeinteLunette',
            },
        ),
        migrations.CreateModel(
            name='TraitementLunette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TraitementLunette', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'TraitementLunettes',
                'verbose_name_plural': 'TraitementLunette',
            },
        ),
        migrations.CreateModel(
            name='Lunette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MatierePremiereLunette', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uranel_django_app.matierepremierelunette')),
                ('PointFocalLunette', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uranel_django_app.pointfocallunette')),
                ('TeinteLunette', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uranel_django_app.teintelunette')),
                ('TraitementLunette', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uranel_django_app.traitementlunette')),
            ],
            options={
                'verbose_name': 'Lunettes',
                'verbose_name_plural': 'Lunette',
            },
        ),
    ]
