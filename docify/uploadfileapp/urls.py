
from django.urls import path, include

from . import views


urlpatterns = [

	path('', views.index, name = "home"),
	path('uploadfile/', views.uploadFile, name = "uploadfile"),
	path('uploadfilesave/', views.uploadFileSave, name = "uploadFileSave")
   

]