# Generated by Django 4.1.1 on 2022-11-09 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0007_alter_dataset_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
