# Generated by Django 5.0.6 on 2024-06-17 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_flan_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flan',
            name='slug',
        ),
    ]