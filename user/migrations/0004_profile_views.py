# Generated by Django 4.1 on 2022-08-08 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_remove_user_is_writer_profile_is_writer"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="views",
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
