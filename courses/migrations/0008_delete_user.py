# Generated by Django 4.0.5 on 2022-08-07 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_rename_user_permission_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
