# Generated by Django 3.1.3 on 2021-02-16 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210216_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trener',
            name='time_work',
            field=models.IntegerField(),
        ),
    ]