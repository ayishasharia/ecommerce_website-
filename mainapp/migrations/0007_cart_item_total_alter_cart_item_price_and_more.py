# Generated by Django 4.2.5 on 2023-10-26 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_cart_item_cart_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_item',
            name='total',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='cart_item',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='cart_item',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
