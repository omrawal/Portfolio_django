# Generated by Django 3.0.3 on 2020-06-24 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='homepage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fav_code', models.CharField(max_length=2000)),
                ('profile_pic', models.ImageField(upload_to='static/profilepic')),
                ('job_profile', models.CharField(max_length=256)),
            ],
        ),
    ]
