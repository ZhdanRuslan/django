# Generated by Django 2.1.5 on 2019-02-11 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_gadgets'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=255)),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Laptop')),
            ],
        ),
    ]