# Generated by Django 3.0.8 on 2020-07-24 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_frontend', '0006_auto_20200724_1954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keywords_Classified',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=512)),
                ('times_classified', models.IntegerField(default=0)),
                ('computer_science', models.IntegerField(default=0)),
                ('mathematics', models.IntegerField(default=0)),
                ('physics', models.IntegerField(default=0)),
                ('astronomy', models.IntegerField(default=0)),
                ('electrical_engineering', models.IntegerField(default=0)),
                ('quantitative_biology', models.IntegerField(default=0)),
                ('statistics', models.IntegerField(default=0)),
                ('economics', models.IntegerField(default=0)),
                ('other', models.IntegerField(default=0)),
            ],
        ),
    ]
