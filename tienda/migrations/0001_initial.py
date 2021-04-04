# Generated by Django 3.1.3 on 2021-04-03 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ColorProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Producto Erasmus Planet', max_length=30)),
                ('codigo', models.CharField(max_length=10)),
                ('precio', models.IntegerField(default=10)),
                ('detalles', models.CharField(max_length=50, null=True)),
                ('talla', models.CharField(choices=[('1', 'XS'), ('2', 'S'), ('3', 'M'), ('4', 'L'), ('5', 'XL'), ('6', 'XXL')], default='', max_length=10, null=True)),
                ('bandera', models.CharField(max_length=30, null=True)),
                ('fecha', models.CharField(max_length=20, null=True)),
                ('color', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='tienda.colorproducto')),
            ],
        ),
    ]
