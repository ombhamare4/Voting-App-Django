# Generated by Django 3.2 on 2021-05-06 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_pollquet_pollquetions_pollquetion'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollquetions',
            name='option1_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pollquetions',
            name='option2_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pollquetions',
            name='option3_count',
            field=models.IntegerField(default=0),
        ),
    ]
