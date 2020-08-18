# Generated by Django 3.0.8 on 2020-08-18 16:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('demo_frontend', '0013_auto_20200818_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keywords',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='keywords_classified',
            name='subject',
        ),
        migrations.AddField(
            model_name='arxiv_titles_classified',
            name='subject',
            field=models.CharField(default=0, max_length=512),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arxiv_titles_in_circulation',
            name='subject',
            field=models.CharField(default=django.utils.timezone.now, max_length=512),
            preserve_default=False,
        ),
    ]
