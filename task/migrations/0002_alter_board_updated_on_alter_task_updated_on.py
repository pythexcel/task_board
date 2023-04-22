# Generated by Django 4.2 on 2023-04-22 06:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
