# Generated by Django 5.0.6 on 2024-06-07 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_product_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_no',
            field=models.IntegerField(null=True),
        ),
    ]
