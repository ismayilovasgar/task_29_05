# Generated by Django 5.0.6 on 2024-06-02 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0003_user"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="User",
            new_name="Article_User",
        ),
    ]
