from django.conf.urls import url , include
from . import views

urlpatterns = [
	#url(r'^$',views.ViewName,name=ViewName)
	#inicio view
	url(r'^$',views.inicio,name='inicio'),
	url(r'^contacto/$',views.contacto,name='contacto'),
	url(r'^somos/$',views.somos,name='somos'),
	url(r'^servicios/$',views.servicios,name='servicios'),
	url(r'^cursos/$',views.cursos,name='cursos'),
]