from django.urls import path
from . import views

urlpatterns = [
    # path 第一个参数:路由,第二个参数:视图函数名
    path('content/', views.content),
    path('index/', views.get_index_page),
    path('detail/<int:article_id>', views.get_detail_page),
]
