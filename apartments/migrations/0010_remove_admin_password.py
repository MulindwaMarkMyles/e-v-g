# Generated by Django 5.0.3 on 2024-05-24 09:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("apartments", "0009_admin_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="admin",
            name="password",
        ),
    ]
