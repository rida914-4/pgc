"""pgic URL Configuration

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
from asset import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^purchase/(?P<voucher_id>\w+\d+)', views.purchase, name='purchase'),
    url(r'sales', views.index, name='index'),
    url(r'stock', views.index, name='index'),
    url(r'asset', views.asset, name='asset'),
    url(r'asset', views.asset, name='asset'),
    url(r'utils', views.index, name='index'),
    url(r'master', views.index, name='index'),
    url(r'', views.index, name='index'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

