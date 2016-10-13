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
import asset
import pgic
urlpatterns = [
    url(r'^$', views.invoice),
    url(r'^admin/', admin.site.urls),
    url(r'^dashboard/$', views.index, name='index'),

    # asset + purchase
    # url(r'^purchase/$', views.invoice, name='purchase'),
    url(r'^purchase/(?P<voucher_id>\w+\d+)$', views.purchase, name='purchase'),
    url(r'^new/$', views.master_detail_new, name='new'),
    url(r'^next/$', views.master_detail_next, name='new'),
    url(r'^post/$', views.post_new, name='new'),

    # reports
    url(r'^reports/$', views.reports, name='reports'),
    url(r'^reports/(?P<file_name>\w+)$', views.pf_pl_invoicedet, name='pf_pl_invoicedet'),
    url(r'rdownload', views.reports_download),

    # user authentication
    # url(r'^accounts/login/$', views.login),
    # url(r'^$', views.login, name='login'), # officialy this page
    url(r'^accounts/auth/$', views.auth_view),
    url(r'^accounts/loggedin/$', views.loggedin),
    url(r'^accounts/logout/$', views.logout),
    url(r'^accounts/invalid/$', views.invalid_login),








    url(r'sales', views.index, name='index'),
    url(r'stock', views.index, name='index'),
    url(r'utils', views.index, name='index'),
    url(r'master', views.index, name='index'),
    # url(r'form', views.Form, name='form'),
    # url(r'purchase', views.purchase),
    url(r'upload', views.copy_of_upload),
    url(r'pdf', views.pdf_report),






    # url(r'forms', views.get_form),
    # url(r'^post/new/$', views.post_new, name='post_new'),
    # url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    #
    url(r'create/$', views.create),
    # url(r'detail/$', views.post_detail),
    # url(r'list/$', views.post_list),
    # url(r'update/$', views.post_update),
    # url(r'delete/$', views.post_delete),
    url(r'thanks', views.index),
    url(r'url', views.test_profile_settings),
    url(r'thanks', views.index),
    url(r'interview', views.interview),


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
