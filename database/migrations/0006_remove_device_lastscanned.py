# Generated by Django 3.1 on 2020-08-31 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_auto_20200831_1322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='lastScanned',
        ),
    ]
