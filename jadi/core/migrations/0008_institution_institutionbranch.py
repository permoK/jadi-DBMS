# Generated by Django 4.2.11 on 2024-05-24 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_userprofile_learninginstitution'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='institutionBranch',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
