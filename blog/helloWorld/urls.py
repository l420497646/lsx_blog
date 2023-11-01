from django.urls import path
from helloWorld.views import hello_world

urlpatterns = [
    # path 第一个参数:路由\第二个参数:视图函数名
    path('hello_world/', hello_world),
]
