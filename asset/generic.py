import os
import shutil
import logging
from django.conf.urls.static import static
import magic

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
media_path = os.path.join(BASE_DIR, 'media')
static_path = os.path.join(BASE_DIR, 'static')
logger = logging.getLogger(__name__)


def listdir(folder_path):
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    if not os.listdir(folder_path) == []:
        return os.listdir(folder_path)
    else:
        return []


def copy_uploaded_images(voucher_id, folder_type):
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
                ftype = magic.from_file(full_file_name)
                if not any(x in ftype for x in ['PNG', 'JPEG', 'GIF']):
                    error_msg = 'The file attached is not an image.'
                    print error_msg
                    print ftype
                    # os.remove(full_file_name)
                    continue
                print 'PIC GTG!'
                shutil.copy(full_file_name, full_file_name_new)
                # os.remove(full_file_name)
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


if __name__ == '__main__':
    # copy_uploaded_images('PL01060321', 'asset/front')
    check_image_type()