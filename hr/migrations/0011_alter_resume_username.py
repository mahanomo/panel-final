# Generated by Django 4.2 on 2025-07-02 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0010_rename_user_resume_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]
