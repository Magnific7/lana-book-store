from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.Index, name='Index'),
    path('Analytics-dashboard/', views.Analytic, name='Analytic'),
    path('crossSelling-app/', views.CrosslingApp, name='CrosslingApp'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)