import yaml, os
from django.conf import settings
from django.test import TestCase
import yaml
from django.conf import settings
import os

# 读取yaml配置文件
filepath = r'D:\study\project__\django_333\first_dj\first_dj\myappconfig.yaml'
with open(filepath, 'r', encoding='utf8') as f:
    res = yaml.load(f, Loader=yaml.FullLoader)
    print(res)
    print(type(res))


os.environ['DJANGO_SETTINGS_MODULE'] = 'myfirstproj.settings'
# static_file_path = os.path.join(settings.BASE_DIR,'static')
#
# print('static_file_path:', static_file_path)
# filename = r'/abc.png'
# filepath = os.path.join(static_file_path, filename)
# print(filepath)
print('basedir:', settings.BASE_DIR)

static_filedir = settings.STATIC_URL
# print('static_filedir',static_filedir)
print('static_filedir', os.path.join(settings.BASE_DIR, 'static'))
print(settings.STATIC_ROOT)
