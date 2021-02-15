# Generated by Django 3.1.6 on 2021-02-15 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_trener'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.user_1')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]