# Generated by Django 5.0 on 2023-12-28 14:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("fullname", models.CharField(max_length=50, unique=True)),
                ("born_date", models.CharField(max_length=100)),
                ("born_location", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "date_modified",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date modified"
                    ),
                ),
                ("date_created", models.DateTimeField(verbose_name="date created")),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("word", models.CharField(max_length=35)),
                ("date_created", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Quote",
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
                ("quote", models.TextField()),
                (
                    "date_modified",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date modified"
                    ),
                ),
                ("date_created", models.DateTimeField(verbose_name="date created")),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="test_app.author",
                    ),
                ),
                (
                    "tags",
                    models.ManyToManyField(related_name="quotes", to="test_app.tag"),
                ),
            ],
        ),
    ]
