# Generated by Django 2.0.13 on 2019-05-11 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0002_auto_20190511_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(max_length=256),
        ),
    ]