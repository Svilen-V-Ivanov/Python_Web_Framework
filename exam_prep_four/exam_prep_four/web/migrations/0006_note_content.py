# Generated by Django 4.1.2 on 2022-10-28 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_note_options_alter_profile_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
