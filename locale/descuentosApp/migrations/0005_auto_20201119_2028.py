# Generated by Django 3.1.3 on 2020-11-19 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('descuentosApp', '0004_guide_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='body',
            field=models.TextField(max_length=255),
        ),
    ]
