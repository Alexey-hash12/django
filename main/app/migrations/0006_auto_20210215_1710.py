# Generated by Django 3.1.3 on 2021-02-15 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210215_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='adress',
            new_name='address',
        ),
    ]
