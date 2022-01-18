# <lecture.urls>==============
#현재 경로 : http://localhost:8000/
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('',TemplateView.as_view(template_name='index.html'), name='home'),
    path('admin/', admin.site.urls),
    path('bbs/', include('bbs.urls')),
]
