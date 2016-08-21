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
        return render_to_response('purchase_invoice.html', context)


def test(request):
    return render_to_response('test.html')