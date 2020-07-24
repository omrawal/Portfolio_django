from django.contrib import admin
from django.urls import path
from . import views
# from . import views, settings
# from django.contrib.staticfiles.urls import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home,name='portfolio-home'),
    path('about/', views.about,name='portfolio-about'),
    path('contact/', views.contact,name='portfolio-contact'),
    path('experience/', views.experience,name='portfolio-experience'),
    # path('login/', views.login,name='portfolio-login'),
    path('project/', views.project,name='portfolio-project'),
]
# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)