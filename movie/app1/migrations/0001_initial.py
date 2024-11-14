# Generated by Django 5.1 on 2024-09-19 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('year', models.IntegerField()),
                ('language', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='img')),
            ],
        ),
    ]
