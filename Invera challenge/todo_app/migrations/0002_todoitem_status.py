# Generated by Django 4.2.7 on 2023-11-30 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]