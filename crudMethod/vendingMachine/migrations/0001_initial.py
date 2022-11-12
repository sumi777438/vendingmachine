# Generated by Django 4.0.6 on 2022-07-23 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vendingMachine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendingMachine_id', models.CharField(max_length=20)),
                ('machine_code', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('capacity', models.IntegerField()),
                ('payment_method', models.CharField(max_length=20)),
            ],
        ),
    ]
