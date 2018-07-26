from django.conf.urls import url
from csvfile import views

urlpatterns = [
    url(r'^sbuset/$', views.sbu_set),
    url(r'^tracentries/(\w+)/(\w+)/(\w+)/$',views.trac_entries)
]