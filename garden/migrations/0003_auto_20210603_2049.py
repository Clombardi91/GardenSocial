# Generated by Django 3.2.4 on 2021-06-03 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('garden', '0002_auto_20210602_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='LightNeeded',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shade', models.CharField(max_length=280)),
            ],
        ),
        migrations.RenameField(
            model_name='growingzone',
            old_name='name',
            new_name='usda_zone',
        ),
        migrations.CreateModel(
            name='GrowingSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=280)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('done', models.BooleanField(default=False)),
                ('plant', models.ManyToManyField(related_name='schedules', to='garden.Plant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
