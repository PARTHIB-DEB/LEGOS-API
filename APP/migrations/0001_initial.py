# Generated by Django 4.1.7 on 2023-03-24 16:06

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="legos",
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
                ("comics", models.TextField()),
                ("names", models.CharField(max_length=5000)),
                ("total", models.IntegerField()),
                ("seller", models.TextField()),
            ],
        ),
    ]
