# Generated by Django 3.0.8 on 2020-08-19 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo_frontend', '0016_arxiv_titles_skipped'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_Billing',
            new_name='User_Extended',
        ),
    ]
