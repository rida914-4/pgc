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
    # url(r'^new_user', views.create),
    url(r'^purchase/(?P<voucher_id>\w+\d+)$', views.purchase, name='purchase'),
    url(r'sales', views.index, name='index'),
    url(r'stock', views.index, name='index'),
    url(r'^invoice$', views.invoice, name='invoice'),
    url(r'utils', views.index, name='index'),
    url(r'master', views.index, name='index'),
    url(r'form', views.Form, name='form'),
    # url(r'purchase', views.purchase),
    url(r'upload', views.copy_of_upload),
    url(r'pdf', views.pdf_report),
    url(r'new_invoice', views.new_invoice),



    #
    # url(r'create/$', views.post_create),
    # url(r'detail/$', views.post_detail),
    # url(r'list/$', views.post_list),
    # url(r'update/$', views.post_update),
    # url(r'delete/$', views.post_delete),
    url(r'your-name', views.get_name),
    url(r'thanks', views.index),
    url(r'url', views.upload_file),
    url(r'/success/url/', views.test),
    url(r'thanks', views.index),


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
