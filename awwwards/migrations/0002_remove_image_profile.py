# Generated by Django 4.0.3 on 2022-03-18 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awwwards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='profile',
        ),
    ]
