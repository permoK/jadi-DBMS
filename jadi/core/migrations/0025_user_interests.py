# Generated by Django 4.2.11 on 2024-06-03 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_rename_course_waitlist_major'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='interests',
            field=models.ManyToManyField(to='core.interest'),
        ),
    ]