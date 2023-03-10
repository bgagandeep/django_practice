# Generated by Django 4.1.6 on 2023-02-19 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Patient",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                ("email", models.EmailField(max_length=100)),
                ("phone", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("zip_code", models.CharField(max_length=100)),
                ("date_of_birth", models.DateField()),
                ("date_created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
