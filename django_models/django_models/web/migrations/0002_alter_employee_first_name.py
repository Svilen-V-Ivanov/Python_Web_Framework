# Generated by Django 4.1.2 on 2022-10-07 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
    ]
