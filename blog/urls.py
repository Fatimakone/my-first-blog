from django.urls import path
from . import views

urlpatterns = [
	#path('', views.acceuil),
	path('', views.listepost),
	]

