# Generated by Django 4.2.11 on 2024-05-20 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_rename_resource_resourcecategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorizedUploader',
            fields=[
                ('uploaderId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.userprofile')),
            ],
        ),
    ]
