# Generated by Django 4.1.1 on 2022-11-09 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0006_alter_dataset_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
