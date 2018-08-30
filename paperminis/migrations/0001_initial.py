# Generated by Django 2.0.5 on 2018-07-31 22:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import paperminis.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', paperminis.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Bestiary',
            fields=[
                ('id', models.AutoField(help_text='Unique ID for this particular creature across whole database.', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Bestiaries',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Creature',
            fields=[
                ('id', models.AutoField(help_text='Unique ID for this particular creature across whole database.', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name of the creature as printed on the mini.', max_length=150)),
                ('img_url', models.TextField(help_text='Url to the image of the creature.')),
                ('size', models.CharField(choices=[('T', 'Tiny'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('H', 'Huge'), ('G', 'Gargantuan')], default='M', help_text='Size of the creature.', max_length=1)),
                ('owner', models.ForeignKey(blank=True, help_text='The owner of the creature.', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CreatureQuantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('bestiary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paperminis.Bestiary')),
                ('creature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paperminis.Creature')),
            ],
        ),
        migrations.AddField(
            model_name='bestiary',
            name='bestiary',
            field=models.ManyToManyField(help_text='A list of creatures belonging to this bestiary.', through='paperminis.CreatureQuantity', to='paperminis.Creature'),
        ),
        migrations.AddField(
            model_name='bestiary',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
