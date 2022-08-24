# Generated by Django 4.1 on 2022-08-20 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0007_alter_user_groups_alter_user_user_permissions"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="course",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                blank=True, default="images/default.jpeg", null=True, upload_to=""
            ),
        ),
    ]
