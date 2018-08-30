# Generated by Django 2.1 on 2018-08-17 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paperminis', '0012_auto_20180817_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printsettings',
            name='paper_format',
            field=models.CharField(choices=[('a4', 'A4'), ('a3', 'A3'), ('letter', 'Letter'), ('legal', 'Legal'), ('tabloid', 'Tabloid')], default='a4', max_length=50),
        ),
    ]
