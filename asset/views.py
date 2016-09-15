import os
import re
import errno
import json
import shutil
from django.shortcuts import render, render_to_response, HttpResponse, HttpResponseRedirect, redirect,get_object_or_404
from django.core.urlresolvers import reverse

from models import *
from generic import *
# Create +----------------------------- views here.
import magic
import logging
from reportlab.pdfgen import canvas
from .forms import NameForm, UploadFileForm
from django.views.generic.edit import FormView
from .forms import FileFieldForm
from django.core.mail import send_mail
from models import Item
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
media_path = os.path.join(BASE_DIR, 'media')
static_path = os.path.join(BASE_DIR, 'static')
logger = logging.getLogger(__name__)


def index(request):
    logger.info('Launching pgc')
    return render_to_response('index.html')


def invoice(request):
    asset_db = VPlInvoice.objects.all()

    context = {
            'assets': asset_db
        }
    logger.info('Asset dictionary %s', context)
    return render_to_response('asset.html', context)


def purchase(request, voucher_id):
    logger.info('First purchase method %s', voucher_id)
    master_dic = dict()
    context = dict()
    # if len(request.body.split('=')) > 0:
    #     voucher_id = request.body.split('=')[0]
    # else:
    #     voucher_id = ''
    logger.info('Getting voucher id from post request %s', voucher_id)
    imagelib_path = os.path.join(static_path, 'asset/lib', voucher_id)
    imagefront_path = os.path.join(static_path, 'asset/front', voucher_id)
    imagebill_path = os.path.join(static_path, 'asset/bills', voucher_id)
    invoice_data = VPlInvoicedet.objects.all().filter(voucher_id=voucher_id)

    for a in invoice_data:
        logger.info('acct_id %s--------------------------------------------,', a.acct_id)
        master_dic['acct_id'] = a.acct_id
        master_dic['stock_name'] = a.stock_name
        master_dic['voucher_date'] = a.voucher_date
        master_dic['particulars'] = a.particulars
        master_dic['stock_code'] = a.stock_code
    logger.info('master dic done')
    if request.method == "GET":
        context = {
                'voucher_id': voucher_id,
                'invoice_data': invoice_data,
                'acct_id': master_dic['acct_id'],
                'stock_name': master_dic['stock_name'],
                'voucher_date': master_dic['voucher_date'],
                'particulars': master_dic['particulars'],
                'imagelib_count': len(listdir(imagelib_path)),
                'imagelib_list': listdir(imagelib_path),
                'imagebill_list': listdir(imagebill_path),
                'imagefront_listt': listdir(imagefront_path),
            }
        logger.info(context)
        return render(request, 'purchase_invoice.html', context)
    else:

        return render(request, 'purchase_invoice.html', context)


def item_list():
    item_list = []
    items = Item.objects.values('description')
    for item in items:
        item_list.append(item['description'])
    return item_list


def pos_list():
    item_list = []
    items = Positions.objects.values('description')
    for item in items:
        item_list.append(item['description'])
    return item_list


def cust_list():
    item_list = []
    items = Custodian.objects.values('description')
    for item in items:
        item_list.append(item['description'])
    return item_list


def new_invoice(request):
    context = {
        'items': item_list(),
        'positions': pos_list(),
        'custodian': cust_list(),

    }
    return render(request, 'new_invoice.html', context)


def Form(request):
    context = {
        'rida': 'PL564646'
    }
    return render(request, 'formm.html', context)

#*********************************************#
#               Working single image upload
#*********************************************#


def upload(request):
    if request.method == "POST":
        logger.info('Upload start ' + '*'*25)
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            logger.info('files --> %s', request.FILES.getlist("files"))
            files_to_upload = request.FILES.getlist("files")
            logger.info('files to be uploaded type %s', files_to_upload)

            folder_type = str(request.POST['folder_type']).replace("_", "/").replace("-", "/")
            logger.info('folder type %s', folder_type)

            voucher_id = request.POST.get("voucher_id")
            logger.info('v %s', voucher_id)
            folder_path = os.path.join(static_path,  voucher_id)
            folder_count = len(listdir(folder_path))
            logger.info('New folder count %s in %s', folder_count, folder_path)

            # check the count in static. Donot want to overwrite

            for count, x in enumerate(files_to_upload):

                def process(f):
                    sub_file = os.path.join(folder_path, voucher_id + '_' + str(count))
                    with open(sub_file, 'wb+') as destination:
                        for chunk in f.chunks():
                            destination.write(chunk)

                if folder_count > 0:
                    count += folder_count
                    process(x)
                    count += 1
                else:
                    process(x)
            copy_uploaded_images(str(voucher_id), str(folder_type))
            logger.info('New folder count %s in %s', folder_count, folder_path)

        else:
            # form = UploadFileForm()
            logger.error('Form does not seem valid %s', form.errors)

        return HttpResponseRedirect(voucher_id)
    else:
        voucher_id = ''
        # form = UploadFileForm()
        # logger.error('Not a POST REQUEST %s', form.errors)
        # return render(request, 'purchase_invoice.html', {'form': form})
        return HttpResponse(voucher_id)


#*********************************************#
#                Helper views
#*********************************************#


def create(request):
    logger.info(request.method)
    if request.method == "POST":
        logger.info('*'*50)
        logger.info(request.POST)
        logger.info('*'*50)
        return render(request, 'test.html', context={})
    else:
        return render(request, 'index.html', context={})


def copy_of_upload(request):
    if request.method == "POST":
        logger.info('Upload start')
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():

            files_to_upload = request.FILES.getlist("files")
            logger.info('folder type %s', files_to_upload)
            folder_type = str(request.POST['folder_type']).replace("_", "/").replace("-", "/")
            logger.info('folder type %s', folder_type)
            voucher_id = request.POST.get("voucher_id")
            logger.info('folder type %s', folder_type)
            folder_path = os.path.join(static_path, folder_type, voucher_id)
            mfolder_path = os.path.join(media_path, folder_type, voucher_id)
            folder_count = len(listdir(folder_path))
            listdir(mfolder_path)
            logger.info('New folder count %s in %s', folder_count, folder_path)

            # check the count in static. Donot want to overwrite

            for count, x in enumerate(files_to_upload):

                def process(f):
                    sub_file = os.path.join(mfolder_path, voucher_id + '_' + str(count))
                    with open(sub_file, 'wb+') as destination:
                        for chunk in f.chunks():
                            destination.write(chunk)

                if folder_count > 0:
                    count += folder_count
                    process(x)
                    count += 1
                else:
                    process(x)
            logger.info('v %s fol %s', voucher_id, folder_type)
            copy_uploaded_images(str(voucher_id), str(folder_type))
            logger.info('New folder count %s in %s', folder_count, folder_path)

        else:
            # form = UploadFileForm()
            logger.error('Form does not seem valid %s', form.errors)

        return HttpResponseRedirect(voucher_id)
    else:
        voucher_id = ''
        # form = UploadFileForm()
        # logger.error('Not a POST REQUEST %s', form.errors)
        # return render(request, 'purchase_invoice.html', {'form': form})
        return HttpResponse(voucher_id)


def handle_uploaded_file(f, folder_path):
    with open(folder_path + '/t', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    logger.info('Upload complete!')


def upload_file(request):
    if request.method == 'POST':
        logger.info('Upload start')
        form = UploadFileForm(request.POST, request.FILES)

        logger.info(' | request value ---> %s :', request.POST.get("your_name"))
        # voucher_id = re.findall(r'PL[0-9]+_[a-z0-9-]+', request.POST.get('value'), re.I)
        # logger.info('voucher id %s', voucher_id)
        # logger.info('request files with name %s :', request.FILES[voucher_id[0]])
        if form.is_valid():
            handle_uploaded_file(request.FILES['files'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'upload.html'  # Replace with your template.
    success_url = '...'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
               logger.info(f)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


def pdf_report(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="sample.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response


def test(request):
    return render(request, 'test.html')


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            data = form.cleaned_data
            logger.info('FORM INFO')
            logger.info('form info date is %s ', data)
            subject = form.cleaned_data['new_date']
            message = form.cleaned_data['item_combo']
            logger.info('item combo is %s ', form.cleaned_data.get('item_combo'))
            # logger.info('form info vid is %s ', data['new_vid'])
            # logger.info('form info item is %s ', data['item_combo'])
            # logger.info('form info parc %s ', data['new_parc'])
            # redirect to a new URL:
            logger.info('redirecting -----------------------')
            return HttpResponseRedirect('/thanks/')
        else:
            logger.error('Form is invalid. Errors are %s', form.errors)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        logger.error('Form has GET request. Errors are %s', form.errors)

    return render(request, 'form.html', {'form': form})


def post_new(request):
    form = NameForm()
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            #  add more fields which are not present in the form
            # post.author = request.user
            # post.published_date = timezone.now()
            # post.save()
            return redirect('/thanks/', pk=post.pk)
    else:
        form = NameForm()
        logger.error('Form has GET request. Errors are %s', form.errors)
    return render(request, 'form.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = NameForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
            # post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = NameForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
