from datetime import datetime, timedelta

from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from app.models import UserModel, TicketModel, Goods
from utils.functions import get_ticket

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')

        if UserModel.objects.filter(username=username).exists():

            User = UserModel.objects.get(username=username)

            if check_password(password,User.password):
                ticket = get_ticket()
                out_date = datetime.now() + timedelta(days=14)
                TicketModel.objects.create(
                    user = User,
                    ticket = ticket,
                    out_date = out_date,
                    )
                response = HttpResponseRedirect(reverse('ttsx:index'))
                response.set_cookie('ticket', ticket, expires=out_date)
                return response
            else:
                msg = '密码错误'
                return render(request,'login.html',{'msg':msg})
        else:
            msg = '密码错误'
            return render(request,'login.html',{'msg':msg})



def index(request):
    if request.method == 'GET':
        user = request.user
        return render(request,'index.html',{'user':user})





def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        cpassword = request.POST.get('cpwd')
        email = request.POST.get('email')
        if not all([username,password,cpassword,email]):
            msg = '参数不能为空'
            return render(request,'register.html',{'msg':msg})
        if password != cpassword:
            msg = '密码不一致'
            return render(request,'register.html',{'msg':msg})
        UserModel.objects.create(
            username = username,
            password = make_password(password),
            email = email,
        )
        return HttpResponseRedirect(reverse('ttsx:login'))


def cart(request):
    if request.method == 'GET':
        return render(request,'cart.html')

def list(request):
    if request.method == 'GET':
        return render(request,'list.html')

def my(request):
    if request.method == 'GET':
        return render(request,'user_center_info.html')

def my_order(request):
    if request.method == 'GET':
        return render(request,'user_center_order.html')

def site(request):
    if request.method == 'GET':
        return render(request,'user_center_site.html')

def detail(request,gid):
    good = Goods.objects.get(gid=gid)
    return render(request,'detail.html',{'good':good,'gid':gid})


