# Generated by Django 3.0.8 on 2020-08-03 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo_frontend', '0010_auto_20200803_0121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_extension',
            old_name='number_classified',
            new_name='times_classified',
        ),
    ]
