# Generated by Django 5.1.3 on 2024-12-25 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing_app", "0007_alter_mailingtrying_status_trying"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailingtrying",
            name="server_response",
            field=models.CharField(max_length=1000),
        ),
    ]
