# Generated by Django 4.0.5 on 2022-08-08 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_alter_user_avatar'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
