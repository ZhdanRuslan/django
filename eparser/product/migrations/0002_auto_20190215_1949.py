# Generated by Django 2.1.5 on 2019-02-15 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Laptop',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Phone',
        ),
    ]
