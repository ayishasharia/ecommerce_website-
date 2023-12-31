# Generated by Django 4.2.5 on 2023-10-22 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_user_1_userf_user_1_gender_user_1_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.IntegerField(null=True)),
                ('p_name', models.CharField(max_length=255, null=True)),
                ('p_category', models.CharField(max_length=255, null=True)),
                ('p_price', models.IntegerField(null=True)),
                ('p_image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
