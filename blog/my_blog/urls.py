from django.urls import path
from .views import content

urlpatterns = [
    # path 第一个参数:路由\第二个参数:视图函数名
    path('content/', content),
]
