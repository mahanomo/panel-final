# Generated by Django 4.2 on 2025-07-02 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0014_define_user_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='define_user',
            name='password_changed',
            field=models.BooleanField(default=False),
        ),
    ]
