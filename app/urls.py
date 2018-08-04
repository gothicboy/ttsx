from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'login/',views.login,name='login'),
    url(r'index/',views.index,name='index'),
    url(r'register/',views.register,name='register'),
    url(r'cart/',views.cart,name='cart'),
    url(r'list/',views.list,name='list'),
    url(r'my/',views.my,name='my'),
    url(r'my_order/',views.my_order,name='my_order'),
    url(r'site/',views.site,name='site'),
    url(r'detail/(\d+)/',views.detail,name='detail'),
]