# Generated by Django 4.2.11 on 2024-05-30 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_alter_usereducationdetails_learning_institution_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='major',
            name='major_abbreviation',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
