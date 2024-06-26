# Generated by Django 5.0.6 on 2024-06-02 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0002_alter_article_author_alter_article_content_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("username", models.TextField(max_length=40, unique=True)),
                ("sluq", models.SlugField(blank=True, editable=False, unique=True)),
            ],
        ),
    ]
