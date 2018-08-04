from django.db import models

# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length=40,unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(max_length=30,unique=True)
    is_delect = models.BooleanField(default=False)


class TicketModel(models.Model):
    user = models.ForeignKey(UserModel)
    ticket = models.CharField(max_length=60)
    out_date = models.DateTimeField()


class Goods(models.Model):      #商品信息
    gid = models.IntegerField(primary_key=True,unique=True)
    gtitle = models.CharField( max_length=20)
    gpic = models.CharField(max_length=200)  #商品图片
    gprice = models.DecimalField(max_digits=7, decimal_places=2)  #总共最多有7位,小数占2位
    gunit = models.CharField(max_length=20, default='500g')     #商品的单位
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = 'tb_goods'

class CartModel(models.Model):
    user = models.ForeignKey(UserModel)  # 关联用户
    goods = models.ForeignKey(Goods)  # 关联商品
    c_num = models.IntegerField(default=1)  # 商品的个数
    is_select = models.BooleanField(default=True)  #  是否选择商品

    class Meta:
        db_table = 'tb_cart'
