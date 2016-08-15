# accounts/urls.py

from django.conf.urls import url

from apps.accounts import views

urlpatterns = [
	url(r'^$', views.index_view, name='accounts.index'),
	url(r'^login/$', views.login_view, name='accounts.login'),
    url(r'^registro/$', views.registro_usuario_view, name='accounts.registro'),
    url(r'gracias/(?P<username>[\w]+)/$', views.gracias_view, name='accounts.gracias'),
	url(r'^logout/$', views.logout_view, name='accounts.logout'),
	url(r'^editar_email/$', views.editar_email, name='accounts.editar_email'),
	url(r'^editar_contrasena/$', views.editar_contrasena, name='accounts.editar_contrasena'),

	
]