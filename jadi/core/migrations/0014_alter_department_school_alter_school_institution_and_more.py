# Generated by Django 4.2.11 on 2024-05-25 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_remove_userprofile_learninginstitution_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.school'),
        ),
        migrations.AlterField(
            model_name='school',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.institution'),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='learningInstitution',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='learningInstitution',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.institution'),
            preserve_default=False,
        ),
    ]
