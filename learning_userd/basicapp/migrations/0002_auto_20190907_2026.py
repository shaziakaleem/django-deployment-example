# Generated by Django 2.2.1 on 2019-09-07 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pics',
            field=models.ImageField(blank=True, upload_to='basic_app/profile_pics'),
        ),
    ]