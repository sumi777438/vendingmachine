# Generated by Django 4.0.6 on 2022-07-24 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendingMachine', '0002_product_transaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendingmachine',
            old_name='address',
            new_name='located_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='vendingMachine',
        ),
        migrations.AddField(
            model_name='product',
            name='vendingMachine',
            field=models.ManyToManyField(to='vendingMachine.vendingmachine'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
