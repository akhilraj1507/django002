from django.urls import path
from . import views

urlpatterns=[
    path('',views.a2,name=''),
    path('newpage/<int:pid>',views.a3,name='newpage'),
    path('preview/<int:pid>',views.carEdit,name='preview'),
    path('delview/<int:cid>',views.carDel,name='delview'),
    path('upload/',views.carUp,name='upload'),
    path('uedt/<int:bid>',views.cedit,name='cedit')
    


]