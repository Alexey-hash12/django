# Generated by Django 3.1.3 on 2021-02-17 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210216_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trener',
            name='staj',
            field=models.CharField(max_length=110),
        ),
    ]
