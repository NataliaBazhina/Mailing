# Generated by Django 5.1.3 on 2025-06-16 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("clients_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="client",
            options={
                "permissions": [("can_view_client", "Может просматривать клиентов")],
                "verbose_name": "клиент",
                "verbose_name_plural": "клиенты",
            },
        ),
    ]
