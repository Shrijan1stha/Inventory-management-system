# Generated by Django 5.0.6 on 2024-05-31 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='department',
            field=models.ManyToManyField(null=True, to='base.department'),
        ),
    ]
