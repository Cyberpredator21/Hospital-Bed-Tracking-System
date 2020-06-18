from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^bed_availability/$', views.bed_availability, name='bed_availability'),
    url(r'^new_bed/$', views.new_bed, name='new_bed'),
    url(r'^nurse_bed_availability/$', views.nurse_bed_availability, name='nurse_bed_availability'),
    url(r'^bed_availability/$', views.bed_count, name='bed_count'),
    url(r'^contact_us/$', views.contact_us, name='contact_us'),
    url(r'^press_report/$', views.press_report, name='press_report'),

    url(r'^patient_list/$', views.patient_list, name='patient_list'),
    url(r'^patient_list/patient_new/$', views.patient_new, name='patient_new'),

    # url(r'^hospital_list/$', views.hospital_list, name='hospital_list'),
    url(r'^nurse_list/$', views.nurse_list, name='nurse_list'),

    url(r'^personal/$', views.personal, name='personal'),
    url(r'^patient_list/personal', views.personal, name='personal'),
    url(r'^admin_hospital_list/$', views.admin_hospital_list, name='admin_hospital_list'),
    url(r'^admin_hospital_list/(?P<pk>[\a-z]+)/delete/$', views.admin_hospital_delete, name='admin_hospital_delete'),
    url(r'^admin_hospital_list/(?P<pk>[\w-]+)/edit/$', views.admin_hospital_edit, name='admin_hospital_edit'),
    url(r'^admin_hospital_list/create/$', views.admin_hospital_new, name='admin_hospital_new'),
    url(r'^nurse_list/$', views.nurse_list, name='nurse_list'),
    url(r'^nurse_list/(?P<pk>\d+)/delete/$', views.nurse_delete, name='nurse_delete'),
    url(r'^nurse_list/(?P<pk>\d+)/edit/$', views.nurse_edit, name='nurse_edit'),
    url(r'^nurse_new/$', views.nurse_new, name='nurse_new'),
    url(r'^nurse_home/',views.nurse_home,name='nurse_home'),
    url(r'^admin_home/', views.admin_home, name='admin_home'),
    url(r'^admin_login/', views.admin_login, name='admin_login'),
    url(r'^bedcount_update/$', views.bedcount_update, name='bedcount_update'),
    url(r'^contact_us/thanks', views.thanks, name='thanks'),
    url(r'^accounts/profile/$', views.foo_view, name='foo_view'),
    url(r'^bed_availability/eBedTrack/view_details', views.view_details, name='view_details'),
    url(r'^privacy_statement', views.privacy_statement, name='privacy_statement'),
    url(r'^legal_notice', views.legal_notice, name='legal_notice'),
    url(r'^home/privacy_statement', views.privacy_statement, name='privacy_statement'),
    url(r'^home/legal_notice', views.legal_notice, name='legal_notice'),
    url(r'^bed_availability/privacy_statement', views.privacy_statement, name='privacy_statement'),
    url(r'^bed_availability/legal_notice', views.legal_notice, name='legal_notice'),
    url(r'^contact_us/privacy_statement', views.privacy_statement, name='privacy_statement'),
    url(r'^contact_us/legal_notice', views.legal_notice, name='legal_notice'),
    url(r'^press_report/privacy_statement', views.privacy_statement, name='privacy_statement'),
    url(r'^press_report/legal_notice', views.legal_notice, name='legal_notice'),
    url(r'^accounts/login/privacy_statement', views.privacy_statement, name='privacy_statement'),
    url(r'^accounts/login/legal_notice', views.legal_notice, name='legal_notice'),
    url(r'^patient/$', views.patient_list, name='patient_list'),
    url(r'^patient/(?P<pk>\d+)/delete/$', views.patient_delete, name='patient_delete'),
    url(r'^patient/(?P<pk>\d+)/edit/$', views.patient_edit, name='patient_edit'),
    url(r'^patient_list/patient_new/$', views.patient_new, name='patient_new'),

]




