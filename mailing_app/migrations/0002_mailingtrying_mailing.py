# Generated by Django 5.1.1 on 2024-10-31 09:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="mailingtrying",
            name="mailing",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="mailing_app.mailing",
            ),
        ),
    ]
