from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'add/$', views.add_image, name='addImage'),
    url(r'^$', views.galeria, name='list'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.loginview, name='login'),
]
