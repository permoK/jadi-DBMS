# Generated by Django 4.2.11 on 2024-05-27 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_drop_auth_tables'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CoreUserProfile',
            new_name='UserProfile',
        ),
    ]