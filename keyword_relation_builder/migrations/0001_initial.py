# Generated by Django 3.0.8 on 2020-10-01 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword_Pairs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword_pair', models.CharField(max_length=512)),
                ('times_classified', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=512)),
                ('times_classified', models.IntegerField(default=0)),
                ('times_skipped', models.IntegerField(default=0)),
            ],
        ),
    ]