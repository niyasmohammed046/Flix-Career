# Generated by Django 5.0 on 2024-01-05 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0006_alter_jobpost_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='slug',
            field=models.SlugField(max_length=40, null=True),
        ),
    ]
