# Generated by Django 2.2.3 on 2019-07-22 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190719_2332'),
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
