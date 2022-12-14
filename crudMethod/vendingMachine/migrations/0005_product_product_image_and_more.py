# Generated by Django 4.0.6 on 2022-08-30 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendingMachine', '0004_alter_vendingmachine_machine_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, default='crudMethod/static/image/sample_product_image.png', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='vendingmachine',
            name='vendMachine_image',
            field=models.ImageField(blank=True, default='crudMethod/static/image/vending_machine.png', null=True, upload_to=''),
        ),
    ]
