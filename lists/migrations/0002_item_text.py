# Generated by Django 4.1.4 on 2022-12-22 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lists", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="text",
            field=models.TextField(default=""),
        ),
    ]
