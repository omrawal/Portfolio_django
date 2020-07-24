from django.db import models
from django.urls import reverse

## Home
class Homepage(models.Model):
    fav_code=models.ImageField(upload_to='codesnippet')
    profile_pic=models.ImageField(upload_to='profilepic')
    job_profile=models.CharField(max_length=256)


## About
class About_cv(models.Model):
    cv=models.FileField(upload_to='cv')
class About_framework(models.Model):
    framework_name=models.CharField(max_length=256)
    f_level=models.PositiveIntegerField()
class About_language(models.Model):
    language_name=models.CharField(max_length=256)
    l_level=models.PositiveIntegerField()
class About_certi(models.Model):
    c_company=models.CharField(max_length=256,default='NaN')
    c_title=models.CharField(max_length=256)
    c_date=models.DateField()
    c_url=models.URLField()
    c_number=models.CharField(max_length=256)
    c_doc=models.FileField(upload_to='certificates')

## Experience
class Experience(models.Model):
    title=models.CharField(max_length=256)
    job_profile=models.CharField(max_length=256)
    description=models.CharField(max_length=500)
    link=models.URLField()
    tech_stack=models.CharField(max_length=256)
    logo=models.ImageField(upload_to='experience_logo')

## Project
class Project(models.Model):
    title=models.CharField(max_length=256)
    logo=models.ImageField(upload_to='project_logo')
    github_link=models.URLField()
    other_link=models.URLField()
    description=models.CharField(max_length=500)
    tech_stack=models.CharField(max_length=256)
