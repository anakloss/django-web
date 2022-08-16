# Generated by Django 2.2 on 2022-08-15 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='availability',
            field=models.BooleanField(default=True, verbose_name='Disponibilidad'),
        ),
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendaApp.Category', verbose_name='Categorias'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(verbose_name='Precio'),
        ),
    ]
