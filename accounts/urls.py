from django.urls import path
from . import views

urlpatterns=[
    path('login/',views.lgn,name='login'),
    path('sign/',views.sgn,name='sign'),
    path('signout/',views.logout,name='signout')
]