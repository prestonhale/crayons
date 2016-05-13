"""voters URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from voters import views

carrier_list = views.CellCarrierViewSet.as_view({
    'get': 'list'
})
carrier_detail = views.CellCarrierViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
	url(r'^$',
        views.VoterList.as_view(),
        name='voter-list'),
	url(r'^(?P<pk>[0-9]+)/$',
        views.VoterDetail.as_view(),
        name='voter-detail'),
	url(r'^validate-phone/$',
        views.validate_phone),
    url(r'^carriers/$', carrier_list, name='carrier-list'),
    url(r'^carriers/(?P<pk>[0-9]+)/$', carrier_detail, name='carrier-detail')
]
