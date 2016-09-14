from django.conf.urls import url
from django.contrib import admin
from asset import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^new_user', views.create),
    # url(r'^purchase/(?P<voucher_id>\w+\d+)$', views.purchase, name='purchase'),
    url(r'sales', views.index, name='index'),
    url(r'stock', views.index, name='index'),
    url(r'^invoice$', views.invoice, name='invoice'),
    url(r'utils', views.index, name='index'),
    url(r'master', views.index, name='index'),
    url(r'form', views.Form, name='form'),
    url(r'^purchase', views.purchase),
    url(r'upload', views.upload),
    url(r'pdf', views.pdf_report),
    url(r'new_invoice', views.new_invoice),
    url(r'test', views.test),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
