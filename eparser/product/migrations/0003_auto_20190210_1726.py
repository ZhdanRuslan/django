# Generated by Django 2.1.5 on 2019-02-10 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_laptop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='phone',
            name='year',
            field=models.IntegerField(),
        ),
    ]