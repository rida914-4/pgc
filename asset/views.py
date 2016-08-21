from django.shortcuts import render, render_to_response
from models import *
# Create your views here.


def index(request):
    return render_to_response('index.html')


def asset(request):
    asset_db = VPlInvoice.objects.all()

    context = {
        'assets': asset_db
    }
    return render_to_response('asset.html', context)


def purchase(request, voucher_id):
    if request.method == 'GET':
        context = {
            'voucher_id': voucher_id
        }
        return render_to_response('purchase_invoice.html', context)
