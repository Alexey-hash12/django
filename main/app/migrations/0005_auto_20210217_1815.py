# Generated by Django 3.1.3 on 2021-02-17 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210217_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trener',
            name='salary',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trener',
            name='time_work',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]