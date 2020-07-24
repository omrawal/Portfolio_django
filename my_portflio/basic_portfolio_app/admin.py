from django.contrib import admin
from basic_portfolio_app.models import Homepage,About_framework,About_language,About_certi,About_cv
from basic_portfolio_app.models import Experience,Project
# Register your models here.
admin.site.register(Homepage)
admin.site.register(About_framework)
admin.site.register(About_language)
admin.site.register(About_certi)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(About_cv)