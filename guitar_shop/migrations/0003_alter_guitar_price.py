# Generated by Django 4.1.5 on 2023-02-20 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guitar_shop', '0002_remove_guitar_iselectric'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitar',
            name='price',
            field=models.IntegerField(),
        ),
    ]
