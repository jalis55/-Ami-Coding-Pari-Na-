# Generated by Django 4.1.1 on 2022-11-09 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0003_dataset'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataset',
            old_name='timestamp',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='dataset',
            old_name='data',
            new_name='input_values',
        ),
        migrations.AlterField(
            model_name='dataset',
            name='user',
            field=models.ForeignKey(default=5.75, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
