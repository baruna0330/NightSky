# Generated by Django 2.2.3 on 2019-07-22 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190722_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='lat',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='lng',
            field=models.TextField(default=''),
        ),
    ]
