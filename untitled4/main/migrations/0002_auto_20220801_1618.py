# Generated by Django 2.2.5 on 2022-08-01 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='position',
            field=models.CharField(choices=[('reader', 'Reader'), ('admin', 'Admin'), ('writer', 'Writers')], default='reader', max_length=10),
        ),
    ]
