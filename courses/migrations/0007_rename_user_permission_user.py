# Generated by Django 4.0.5 on 2022-08-07 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('oauth2_provider', '0006_alter_application_client_secret'),
        ('courses', '0006_rename_user_user_permission'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_permission',
            new_name='User',
        ),
    ]
