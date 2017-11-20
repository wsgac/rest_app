from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^movies/', views.MoviesView.as_view(), name='movies'),
    url(r'^movie/([0-9]*)$', views.MovieView.as_view(), name='movie'),
    url(r'^persons/', views.PersonsView.as_view(), name='persons'),
    url(r'^person/([0-9]*)$', views.PersonView.as_view(), name='person'),
]
