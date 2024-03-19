# Generated by Django 4.2.6 on 2024-02-12 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_incomingzulipmessage"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ZulipImgRequest",
        ),
        migrations.AddField(
            model_name="app",
            name="on_screen_duration_seconds",
            field=models.IntegerField(default=60),
        ),
    ]