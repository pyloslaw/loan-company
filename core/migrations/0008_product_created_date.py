# Generated by Django 4.0.4 on 2022-05-23 17:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_product_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2022, 5, 23, 17, 14, 16, 5376, tzinfo=utc)),
        ),
    ]
