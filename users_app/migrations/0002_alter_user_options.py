# Generated by Django 5.1.3 on 2025-06-16 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "permissions": [
                    ("can_view_user", "Может просматривать пользователей"),
                    ("can_delete_user", "Может удалить пользователя"),
                ],
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
    ]
