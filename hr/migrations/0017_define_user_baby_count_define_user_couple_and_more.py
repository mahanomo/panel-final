# Generated by Django 4.2 on 2025-07-02 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0016_alter_define_user_password_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='define_user',
            name='baby_count',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='define_user',
            name='couple',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='define_user',
            name='father_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='define_user',
            name='id_card',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
