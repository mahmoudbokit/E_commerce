# Generated by Django 4.1.3 on 2022-11-14 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineShop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=350)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('State', models.CharField(max_length=350)),
                ('zipcode', models.CharField(max_length=350)),
                ('date_command', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
