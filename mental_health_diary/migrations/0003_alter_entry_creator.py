# Generated by Django 4.1.3 on 2022-11-10 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("mental_health_diary", "0002_alter_entry_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="entry",
            name="creator",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]