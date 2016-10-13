import re
import os
import shutil
import logging
from django.conf.urls.static import static
import urllib2
import urllib
from models import Item
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
media_path = os.path.join(BASE_DIR, 'media')
static_path = os.path.join(BASE_DIR, 'static')
logger = logging.getLogger(__name__)


def listdir(folder_path):
    if 'front' in folder_path:
        folder_path = folder_path.replace('front', '')
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    if not os.listdir(folder_path) == []:
        return os.listdir(folder_path)
    else:
        return []

#In start of a project, create these dirs once

# *************************************************** #
#                   Invoice                           #
# *************************************************** #
def item_list():
    item_list = []
    items = Item.objects.all().values_list('cat_id', 'description')
    print items
    for item in items:
        item_list.append(item['description'])
    return item_list


def createdir(folder_path):

    def x(path):
        if not os.path.exists(path):
            os.mkdir(path)
    x(media_path)
    x(static_path)
    for a in ['bills', 'lib', 'specs']:
        x(os.path.join(media_path, 'asset', a))
        x(os.path.join(static_path, 'asset', a))


def checkfrontpic(folder_path, voucher_id):
    folder_path = folder_path.replace('front', '')
    current_list = map(str, listdir(folder_path))

    count_list = []
    regex = re.compile(".*_0$")
    old_front_pic = [m.group(0) for l in current_list for m in [regex.search(l)] if m]
    for image_name in current_list:
        count_list.append(str(re.findall(r'_.*$', image_name, re.I)[0]).replace('_', ''))

    if old_front_pic:
        count_list = map(int, count_list)
        max_number = max(count_list)
        os.rename(os.path.join(folder_path, '{}_0'.format(voucher_id)),
                  os.path.join(folder_path, '{}_{}'.format(voucher_id, max_number + 1)))
    else:
        print 'no old pic'


def copy_uploaded_images(voucher_id, folder_type):
    folder_type = folder_type.replace('front', '')
    logger.info('type voucher %s', type(voucher_id))
    logger.info('type folder %s', type(folder_type))
    copy_from = os.path.join(media_path, folder_type, voucher_id)
    copy_to = os.path.join(static_path, folder_type, voucher_id)
    try:
        for file_name in listdir(copy_from):
            if ' ' in file_name:
                os.rename(os.path.join(copy_from, file_name), os.path.join(copy_from, file_name.replace(" ", "")))
                file_name = file_name.replace(" ", "")

            full_file_name = os.path.join(copy_from, file_name)
            full_file_name_new = os.path.join(copy_to, file_name)
            print full_file_name
            print full_file_name_new
            if os.path.isfile(full_file_name):
                # ftype = magic.from_file(full_file_name)
                # if not any(x in ftype for x in ['PNG', 'JPEG', 'GIF']):
                #     error_msg = 'The file attached is not an image.'
                #     print error_msg
                #     print ftype
                #     # os.remove(full_file_name)
                #     continue
                print 'PIC GTG!'
                shutil.copy(full_file_name, full_file_name_new)
                os.remove(full_file_name)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        # if e.errno == errno.ENOTDIR:
        #     shutil.copy(copy_from, copy_to)
        # else:
        print 'Directory not copied. Error: %s' % e


def check_image_type():
    ftype = magic.from_file('/home/rah/1.gif')
    print ftype
    if 'JPEG' in ftype:
        print ftype
# *************************************************** #
#                  Reports                            #
# *************************************************** #

def reports_download():
    report_url = '''http://192.168.100.3:7001/reports/rwservlet?server=RptSrvCS+report=s:\\apps\\oracle11g\\art\\reports\\voucher.rdf+userid=click_art/pass@psm+desformat=pdf+DESTYPE=cache+p_voucher_id=CP090386'''
    logger.info('Launching pgc')
    try:
        # html = response.read()
        #-----
        # logger.info('Report downloaded')
        # testfile = urllib.URLopener()
        # testfile.retrieve(report_url, "new")
        urllib.urlretrieve(report_url, "fffffffffffffffffffffff")
        # file_name = wget.download(report_url)
        # print 'File name is ' + file_name
    except:
        print 'no'
        # response = urllib2.urlopen(report_url)
        # html = response.read()



if __name__ == '__main__':
    # copy_uploaded_images('PL01060321', 'asset/front')
    checkfrontpic()