from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.my_memoUI, name='my_memoUI'),
]
