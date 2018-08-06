from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'login/',views.login,name='login'),
    url(r'index/',views.index,name='index'),
    url(r'register/',views.register,name='register'),
    url(r'^cart/$',views.cart,name='cart'),
    url(r'list/',views.list,name='list'),
    url(r'my/',views.my,name='my'),
    url(r'^my_order/$',views.my_order,name='my_order'),
    url(r'site/',views.site,name='site'),
    url(r'detail/(\d+)/',views.detail,name='detail'),
    url(r'^addtocart/$',views.addtocart,name='addtocart'),
    url(r'^goodsCount/$',views.goodsCount,name='goodsCunt'),
    url(r'^addcart/$',views.addcart,name='addcart'),
    url(r'^subcart/$',views.subcart,name='subcart'),
    url(r'^place_order/$',views.place_order,name='place_order'),
]