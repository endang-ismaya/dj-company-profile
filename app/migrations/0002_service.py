# Generated by Django 5.1.6 on 2025-03-06 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
