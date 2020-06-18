"""emergencyBedTrackingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('eBedTrack.urls', namespace='eBedTrack')),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^user/password/reset/$',
        views.password_reset,
        {'post_reset_redirect': '/user/password/reset/done/'},
        name='password_reset'),
    url(r'^user/password/reset/done/$',
        views.password_reset_done,  name='password_rest_done'),
    url(r'^user/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        views.password_reset_confirm,
        {'post_reset_redirect': '/user/password/done/'},  name='password_reset_confirm'),
    url(r'^user/password/done/$',
        views.password_reset_complete,  name='password_reset_complete'),

    # ...
]


