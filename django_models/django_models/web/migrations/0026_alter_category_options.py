# Generated by Django 4.1.2 on 2022-10-09 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0025_alter_employee_options_department_created_on_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]