# Generated by Django 4.0.5 on 2022-06-19 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hood',
            name='zoneImage',
            field=models.ImageField(default='default.png', upload_to='zonePics'),
        ),
    ]