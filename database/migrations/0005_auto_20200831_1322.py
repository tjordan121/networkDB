# Generated by Django 3.1 on 2020-08-31 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_auto_20200831_1152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='hostName',
            new_name='hostname',
        ),
    ]