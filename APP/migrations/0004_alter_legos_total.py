# Generated by Django 4.1.7 on 2023-03-29 05:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("APP", "0003_alter_legos_total"),
    ]

    operations = [
        migrations.AlterField(
            model_name="legos",
            name="total",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
