# Generated by Django 3.2 on 2021-05-04 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_pollquetions_pollquetion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pollquetions',
            old_name='pollquetion',
            new_name='pollquet',
        ),
    ]