# Generated by Django 4.2.15 on 2024-10-06 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_remove_orders_phone2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='mainapp.category'),
        ),
        migrations.AlterField(
            model_name='userproductorder',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.product'),
        ),
        migrations.AlterField(
            model_name='userproductorder',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
