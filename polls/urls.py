from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^results/(?P<pk>[0-9]+)/$', views.ResultsView.as_view(), name='results'),
    url(r'^vote/(?P<question_id>[0-9]+)/$', views.vote, name='vote'),
]

