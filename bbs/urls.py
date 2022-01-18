# <bbs.urls>==============
from django.urls import path
from bbs import views

app_name='bbs'

urlpatterns = [
    path('b_list/', views.b_list, name='b_list'),
    path('<int:board_id>/detail/', views.b_detail, name='detail'),
    path('create/', views.b_create, name='b_create'),
    path('create_process/', views.b_create_process, name='b_create_process'),
    path('<int:board_id>/likeclick/', views.likeclick, name='likeclick'),
]
