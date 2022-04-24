# Generated by Django 4.0.1 on 2022-04-22 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contents", "0001_initial"),
        ("star_ratings", "0002_alter_rating_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rating",
            name="content",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="contents.content",
            ),
        ),
    ]
