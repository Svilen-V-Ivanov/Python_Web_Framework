# Generated by Django 4.1.3 on 2022-11-05 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('seniority_level', models.CharField(choices=[('Junior', 'Junior'), ('Regular', 'Regular'), ('Senior', 'Senior')], max_length=30)),
            ],
        ),
    ]
