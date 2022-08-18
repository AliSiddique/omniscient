# Generated by Django 4.1 on 2022-08-17 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0003_contact"),
    ]

    operations = [
        migrations.CreateModel(
            name="BecomeWriter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="article",
            name="category",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Economy", "Economy"),
                    ("Finance", "Finance"),
                    ("Politics", "Politics"),
                    ("Technology", "Technology"),
                    ("Sports", "Sports"),
                    ("Uni", "University"),
                    ("Media", "Media"),
                ],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="description",
            field=models.CharField(max_length=500, null=True),
        ),
    ]