# Generated by Django 2.0.5 on 2018-08-02 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paperminis', '0002_auto_20180801_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='creaturequantity',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
