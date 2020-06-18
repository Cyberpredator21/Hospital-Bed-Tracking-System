from django.conf.urls import url
from . import views

urlpatterns = [
   # url(r'^$', views.nurse_home, name='nurse_home'),
  #  url(r'^nurse_home/$', views.nurse_home, name='nurse_home'),
    url(r'^patient_list/$', views.patient_list, name='patient_list'),
    url(r'^patient_details/$', views.patient_det, name='patient_det'),
    url(r'^accounts/profile/$', views.nurse_home, name='nurse_home'),

 ]


