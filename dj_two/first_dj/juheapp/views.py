from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
import requests, os, hashlib, yaml
from django.conf import settings
from first_dj import settings
from django.views import View
from utils.responseutil import UtilMixin
from utils.responseutil import ResponseMixin


def hellojuhe(request):
    url = "http://v.juhe.cn/dream/category?fid=%E6%9D%9C%E5%B0%91%E6%AF%85&key=cad5055003636967696a2c0d81fca82c"
    res = requests.get(url)
    if res.status_code == 200:
        return HttpResponse(res.text)
    else:
        return HttpResponse('没有获取到数据')


def testrequest(request):
    print('请求方法:', request.method)
    print('客户端信息:', request.META)
    print('get请求参数:', request.GET)
    print('请求头:', request.headers)
    print('cookie:', request.COOKIES)
    return JsonResponse({'请求方法': request.method,
                         '客户端信息': 'ssss',
                         '请求头': 'ssss',
                         'cookie': request.COOKIES.__str__()
                         })


def image(request):
    if request.method == 'GET':
        filepath = os.path.join(settings.STATIC_ROOT_SELF, 'abc.png')
        f = open(filepath, 'rb')
        # with open(filepath,'tb')as f:
        #     return HttpResponse(content=f.read(), content_type='image/png')
        return FileResponse(f, content_type='image/jpg')
    elif request.method == "POST":
        return HttpResponse('这是post请求')
    else:
        return HttpResponse(request.method + "方法没有实现")


class ImageView(View, UtilMixin):
    def get(self, request):
        filepath = os.path.join(settings.STATIC_ROOT_SELF, 'abc.png')
        f = open(filepath, 'rb')
        # with open(filepath,'tb')as f:
        #     return HttpResponse(content=f.read(), content_type='image/png')
        return FileResponse(f, content_type='image/jpg')

    # def post(self, request):
    #     #     # return HttpResponse('这是post请求')
    #     #     # return self.get(request)
    #     #     file_obj=request.FILES.get('file',None)
    #     #     print(file_obj.name)
    #     #     print(file_obj.size)
    #     #
    #     #
    #     #     files = request.FILES
    #     #     print('6666666我在views文件',type(files))
    #     #     for key,value in files.items():
    #     #         print(777,key)
    #     #         print(888,value)
    #     #     return HttpResponse('测试.123..')

    # def post(self, request):    # 张锦涛写的
    #     # 获取文件 返回 key(文件名),value(文件内容)对象
    #     files = request.FILES
    #     response = []
    #     for key, value in files.items():
    #         content = value.read()
    #         md5 = hashlib.md5(content).hexdigest()
    #         path = os.path.join(STATIC_ROOT_SELF, md5 + '.jpg')
    #         with open(path, 'wb') as f:
    #             f.write(content)
    #         response.append({
    #             'name': key,
    #             'md5': md5
    #         })
    #     message = 'post message success'
    #     # response = utils.response.wrap_json_response(message=message)
    #     response = self.wrap_json_response(data=response,
    #                                        code=utils.response.ReturnCode.SUCCESS,
    #                                        message=message)
    #     return JsonResponse(data=response, safe=False)
    def post(self, request):
        # 获取request的文件
        files1 = request.FILES
        # class 'django.utils.datastructures.MultiValueDict'
        # print(type(files))
        picdir = settings.UPLOAD_PIC_DIR

        # 以字典的形式获取filename和内容
        for key, value in files1.items():
            filename = os.path.join(picdir, key[-8:])  # 取名
            UtilMixin.savepic(filename, value.read())  # 保存

            return JsonResponse(UtilMixin.wrapdic({'filename': key[-8:]}))  # return filename倒数8位
        return HttpResponse('代表files里面没有内容')

    def delete(self, request):
        picname = request.GET.get('name')
        picdir = settings.UPLOAD_PIC_DIR
        print(666666, picname,picdir)
        pic_full_path = os.path.join(picdir, picname)
        if not os.path.exists(pic_full_path):
            return HttpResponse('图片不存在')
        else:
            return HttpResponse('删除成功')

    # def delete(self, request):
    #     # 取出文件名字
    #     md5 = request.GET.get('md5')
    #     # 判断这个名字存不存在
    #     img_name = md5 + '.jpg'
    #     # 文件路径
    #     path = os.path.join(IMAGES_DIR, img_name)
    #     if os.path.exists(path):
    #         os.remove(path)
    #         message = 'remove success.'
    #     else:
    #         message = 'file(%s) not found.' % img_name
    #         # response = utils.response.wrap_json_response(message=message)
    #     response = self.wrap_json_response(code=utils.response.ReturnCode.SUCCESS,
    #                                        message=message)
    #     return JsonResponse(data=response, safe=False)

    # def put(self, request):
    #     message = 'put message success'
    #     # response = utils.response.wrap_json_response(message=message)
    #     response = self.wrap_json_response(message=message)
    #     return JsonResponse(data=response, safe=False)


class ImageText(View, ResponseMixin, ):
    # def get(self,request):
    #     filepath = os.path.join(settings.STATIC_ROOT_SELF, 'ac.png')
    #     if os.path.exists(filepath):
    #         f = open(filepath, 'rb')
    #         return FileResponse(f, content_type='image/jpg')
    #     else:
    #         return JsonResponse(data={'code':4040,'des':'没有找到图片'})

    # def get(self,request):
    #     return render(request,'imagetext.html',{'des':'图片描述','url':'/api/v1.0/apps/image/'})

    # 提取公共的状态码信息
    # def wrapjson(self,response):
    #     response['code']=1000
    #     response['codedes']='没发现问题'
    #     return response

    def get(self, request):
        # return JsonResponse(data={'url': 'xxxxx', 'des': '我很好',
        #                           'code': 1000, 'codedes': '没发现问题'})

        # return JsonResponse(data=self.wrapjson({'url': 'xxxxx', 'des': '我很好',
        #                           }))
        # return JsonResponse(data=responseutil.wrap_response({'url': 'xxxxx', 'des': '我很好'
        #                           }))
        # ? 为何wrap_response 不能独立出来,变成一个类, 让所有 xxxView 都继承呢?
        return JsonResponse(data=self.wrap_response({'url': 'xxxxx', 'des': '我很好', 'code': 2002}))


def apps(request):
    # return JsonResponse(['微信', '支付宝','钉钉','王者荣耀'],safe=False, )
    # # return JsonResponse({'name': ['微信', '支付宝', '钉钉', '王者荣耀']}, safe=True, )
    if request.method == "POST":
        return HttpResponse('逗你玩..')
    filepath = r'D:\first_dj\first_dj\first_dj\myappconfig.yaml'
    with open(filepath, 'r', encoding='utf8') as f:
        res = yaml.load(f, Loader=yaml.FullLoader)
    return JsonResponse(res, safe=False)
