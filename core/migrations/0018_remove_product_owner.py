# Generated by Django 4.0.4 on 2022-05-27 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_product_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='owner',
        ),
    ]
