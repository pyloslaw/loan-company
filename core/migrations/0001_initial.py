# Generated by Django 4.0.4 on 2022-05-23 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=50)),
                ('building_no', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(choices=[('CC', 'Credit Card'), ('L1', 'Loan - to 10 000'), ('L2', 'Loan - over 10 000')], default='L1', max_length=2)),
                ('some_stuff', models.CharField(max_length=30)),
                ('some_st2uff', models.CharField(max_length=30)),
                ('some_stu2ff', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Workplace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_nip', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('salaty', models.IntegerField()),
                ('position', models.CharField(max_length=50)),
                ('phone_no', models.IntegerField(unique=True)),
                ('adress', models.ManyToManyField(to='core.adress')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('social_security_no_pesel', models.IntegerField(unique=True, verbose_name='PESEL')),
                ('id_passport', models.CharField(max_length=10, unique=True, verbose_name='ID serial number or Passport serial number')),
                ('martial_status', models.CharField(choices=[('md', 'maiden'), ('bc', 'bachelor'), ('dv', 'divorcee'), ('mr', 'married'), ('wd', 'widow')], max_length=2)),
                ('phone_no', models.IntegerField(unique=True)),
                ('adress', models.ManyToManyField(to='core.adress')),
                ('product', models.ManyToManyField(to='core.product')),
                ('workplace', models.ManyToManyField(to='core.workplace')),
            ],
        ),
    ]
