# Generated by Django 4.1.3 on 2022-11-10 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mental_health_diary", "0005_article_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="category",
            field=models.CharField(max_length=32, null=True),
        ),
    ]
