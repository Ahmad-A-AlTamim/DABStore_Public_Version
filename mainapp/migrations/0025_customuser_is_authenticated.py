# Generated by Django 4.2.15 on 2024-10-20 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0024_remove_customuser_is_authenticated'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_authenticated',
            field=models.BooleanField(default=False),
        ),
    ]