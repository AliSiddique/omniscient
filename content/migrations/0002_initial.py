# Generated by Django 4.1 on 2022-08-06 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("payment", "0001_initial"),
        ("content", "0001_initial"),
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="profile",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="user.profile",
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="favourites",
            field=models.ManyToManyField(
                blank=True, default=None, related_name="favourites", to="user.profile"
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="pricing_tiers",
            field=models.ManyToManyField(blank=True, to="payment.pricing"),
        ),
        migrations.AddField(
            model_name="article",
            name="writer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="user.profile",
            ),
        ),
    ]