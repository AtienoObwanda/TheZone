# Generated by Django 4.0.5 on 2022-06-17 19:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hood', '0001_initial'),
        ('members', '0002_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('profileImage', models.ImageField(default='default.png', upload_to='projectPics')),
                ('phone', models.IntegerField(blank=True, default=0, null=True)),
                ('idNum', models.IntegerField(blank=True, default=0, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.hood')),
            ],
        ),
    ]
