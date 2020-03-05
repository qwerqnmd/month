from django.urls import path
from juheapp import views

urlpatterns = [
    path('juhe', views.hellojuhe),
    path('test/', views.testrequest),
    # 图片
    path('image/', views.image),
    # 图片,升级版
    path('image1/', views.ImageView.as_view()),
    # 图文
    path('imagetext/', views.ImageText.as_view()),
    path('', views.apps)

]
