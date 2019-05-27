from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='CDAT-home'),
    path('analysis/', views.analysis, name='CDAT-analysis'),
    path('analysis/file', views.file_changed, name='CDAT-analysis-file'),

]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)