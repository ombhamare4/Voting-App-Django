# Generated by Django 3.2 on 2021-05-07 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210506_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollquetions',
            name='option1',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='pollquetions',
            name='option2',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='pollquetions',
            name='option3',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='pollquetions',
            name='pollquetion',
            field=models.CharField(max_length=120),
        ),
    ]
