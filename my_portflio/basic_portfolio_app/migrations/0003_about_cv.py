# Generated by Django 3.0.3 on 2020-06-25 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_portfolio_app', '0002_about_certi_about_framework_about_language_experience_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_cv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv', models.FileField(upload_to='')),
            ],
        ),
    ]
