# Generated by Django 2.2.12 on 2022-08-05 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serviceApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'servicio', 'verbose_name_plural': 'servicios'},
        ),
    ]