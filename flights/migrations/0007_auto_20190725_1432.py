# Generated by Django 2.2.2 on 2019-07-25 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0006_auto_20190623_0714'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='date',
            new_name='check_in',
        ),
    ]
