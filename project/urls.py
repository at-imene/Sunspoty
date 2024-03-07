from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	# path('directory/index.html', views.upload_file),
	path("", views.upload_file, name="homepage"),
    path("dbscanAlgo", views.dbscanAlgo, name="dbscanAlgo"),
	path("classification", views.navigate_to_classification_page, name="Classification Page"),
	path("classificationModel", views.classificationModel, name="classificationModel"),
	path("about", views.navigate_to_about_page, name="About Page"),
	path("help", views.navigate_to_help_page, name="Help Page"),
	
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)