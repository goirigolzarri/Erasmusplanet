# Generated by Django 3.1.3 on 2021-04-03 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('descuentosApp', '0022_auto_20210403_1532'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CategoriaProducto',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='color',
        ),
        migrations.DeleteModel(
            name='ColorProducto',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
