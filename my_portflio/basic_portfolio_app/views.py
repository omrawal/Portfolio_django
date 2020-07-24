from django.shortcuts import render
from django.http import HttpResponse
from basic_portfolio_app.models import Homepage,About_framework,About_language,About_certi,Experience,Project,About_cv
# Create your views here.
# def home(request):
#     return HttpResponse('<h1>This is Portfolio Home</h1>')




def home(request):
    homepage_data=Homepage.objects.all()
    return render(request,'basic_portfolio_app/home.html',{'homepage_data':homepage_data})
def about(request):
    about_certi=About_certi.objects.all()
    about_framework=About_framework.objects.all()
    about_language=About_language.objects.all()
    about_cv=About_cv.objects.all()
    return render(request,'basic_portfolio_app/about.html',{'about_certi':about_certi,'about_framework':about_framework,'about_language':about_language,'about_cv': about_cv})
def experience(request):
    experience_data=Experience.objects.all()
    return render(request,'basic_portfolio_app/experience.html',{'experience_data':experience_data})
def project(request):
    project_data=Project.objects.all()
    return render(request,'basic_portfolio_app/project.html',{'project_data':project_data})
def contact(request):
    return render(request,'basic_portfolio_app/contact.html')
# def login(request):
#     return render(request,'basic_portfolio_app/login.html')