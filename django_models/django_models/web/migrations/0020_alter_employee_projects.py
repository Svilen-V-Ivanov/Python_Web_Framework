# Generated by Django 4.1.2 on 2022-10-07 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0019_project_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='projects',
            field=models.ManyToManyField(related_name='employees', to='web.project'),
        ),
    ]
