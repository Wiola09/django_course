# Generated by Django 5.1.2 on 2024-10-26 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_create_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='word_count',
            field=models.IntegerField(blank=True, default=''),
        ),
    ]
