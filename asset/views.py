import os
from django.shortcuts import render, render_to_response, HttpResponse, HttpResponseRedirect
from models import *
from asset.forms import ProfileForm
from asset.models import Profile
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
    master_dic = dict()
    invoice_data = VPlInvoicedet.objects.all().filter(voucher_id=voucher_id)

    for a in invoice_data:
        master_dic['acct_id'] = a.acct_id
        master_dic['stock_name'] = a.stock_name
        master_dic['voucher_date'] = a.voucher_date
        master_dic['particulars'] = a.particulars
        master_dic['stock_code'] = a.stock_code


    if request.method == 'GET':
        context = {
                'voucher_id': voucher_id,
                'invoice_data': invoice_data,
                'acct_id': master_dic['acct_id'],
                'stock_name': master_dic['stock_name'],
                'voucher_date': master_dic['voucher_date'],
                'particulars': master_dic['particulars']

            }
        return render(request, 'purchase_invoice.html', context)


def Form(request):
    context = {
        'rida': 'PL564646'
    }
    return render(request, 'formm.html', context)


def singleUpload(request, voucher_id):
    folder = '/home/rah/PycharmProjects/pgic/media/' + voucher_id + '/'
    for count, x in enumerate(request.FILES.getlist("files")):
        folder = '/home/rah/PycharmProjects/pgic/media/' + voucher_id + '/'

        def process(f):
            if not os.path.isdir(folder):
                os.makedirs(folder)
            with open(folder + voucher_id, 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
        if count == 0:
            process(x)
            continue
    return HttpResponseRedirect('/purchase/' + voucher_id)


def Upload(request, voucher_id):
    for count, x in enumerate(request.FILES.getlist("files")):
        folder = '/home/rah/PycharmProjects/pgic/media/' + voucher_id + '/'

        def process(f):
            if not os.path.isdir(folder):
                os.makedirs(folder)
            with open(folder + str(count), 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
        process(x)
    return HttpResponseRedirect('/purchase/' + voucher_id)



