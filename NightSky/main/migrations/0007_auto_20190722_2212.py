# Generated by Django 2.2.3 on 2019-07-22 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190722_2209'),
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
