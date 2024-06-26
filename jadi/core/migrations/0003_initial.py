# Generated by Django 4.2.11 on 2024-05-25 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_delete_department_delete_lecturer_delete_note_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoreUserProfile',
            fields=[
                ('profileId', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.TextField()),
                ('fullName', models.TextField()),
                ('email', models.EmailField(max_length=256)),
                ('courseMajor', models.TextField()),
                ('isStudent', models.BooleanField()),
                ('isLecturer', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'core_userprofile',
            },
        ),
    ]
