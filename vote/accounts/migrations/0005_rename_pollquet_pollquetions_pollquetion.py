# Generated by Django 3.2 on 2021-05-04 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_pollquetion_pollquetions_pollquet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pollquetions',
            old_name='pollquet',
            new_name='pollquetion',
        ),
    ]
