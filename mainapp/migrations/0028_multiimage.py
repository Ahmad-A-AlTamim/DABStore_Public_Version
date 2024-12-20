# Generated by Django 4.2.15 on 2024-10-21 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0027_remove_customuser_email_remove_customuser_otp'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultiImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product/%Y/%m/%d/%H/%M/%S')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product')),
            ],
        ),
    ]
