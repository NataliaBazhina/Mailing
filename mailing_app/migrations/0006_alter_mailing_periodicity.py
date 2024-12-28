# Generated by Django 5.1.3 on 2024-12-23 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing_app", "0005_mailing_time_next_mailing"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="periodicity",
            field=models.CharField(
                choices=[
                    ("D", "Раз в день"),
                    ("W", "Раз в неделю"),
                    ("M", "Раз в месяц"),
                ],
                default="W",
                max_length=1,
                verbose_name="периодичность",
            ),
        ),
    ]