# Generated by Django 4.2.15 on 2024-10-20 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0020_alter_customuser_whatsapp'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, default='test@mail.com', max_length=254),
        ),
    ]
