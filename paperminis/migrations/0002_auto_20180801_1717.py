# Generated by Django 2.0.5 on 2018-08-01 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paperminis', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bestiary',
            old_name='bestiary',
            new_name='creatures',
        ),
        migrations.AlterField(
            model_name='creature',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='creature',
            name='img_url',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='creature',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='creature',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='creature',
            name='size',
            field=models.CharField(choices=[('T', 'Tiny'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('H', 'Huge'), ('G', 'Gargantuan')], default='M', max_length=1),
        ),
    ]
