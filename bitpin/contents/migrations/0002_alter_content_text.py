# Generated by Django 4.0.1 on 2022-05-07 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='text',
            field=models.TextField(blank=True, max_length=500, verbose_name='Content field'),
        ),
    ]
