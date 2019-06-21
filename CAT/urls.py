from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='CAT-home'),
    path('inputdata/', views.inputdata, name='CAT-inputdata'),
    path('crashstatistics/', views.crashstatistics, name='CAT-crashstatistics'),
    path('cmfoptimizer/', views.cmfoptimizer, name='CAT-cmfoptimizer'),
    path('inputdata/file', views.file_changed, name='CAT-inputdata-file'),

]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)