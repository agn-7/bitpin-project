# Generated by Django 4.0.1 on 2022-05-07 21:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0002_alter_content_text'),
        ('star_ratings', '0004_alter_userrating_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='content',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='contents.content'),
            preserve_default=False,
        ),
    ]
