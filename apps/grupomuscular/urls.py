from django.conf.urls import url, include
from apps.grupomuscular.views import index, GrupoListView, GrupoDetailView

urlpatterns = [
    url(r'^$', index),
    url(r'^lista/$', GrupoListView.as_view(), name='grupo-list'),
    url(r'^(?P<pk>[-_\w]+)/$', GrupoDetailView.as_view(), name='grupo-detail'),
]
