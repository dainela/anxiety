# Generated by Django 5.0.1 on 2024-11-19 00:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0021_rename_gameresult_distraction'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Distraction',
            new_name='Defusion',
        ),
    ]