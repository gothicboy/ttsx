from datetime import datetime

import re
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.utils.deprecation import MiddlewareMixin

from app.models import TicketModel


class Usermiddleware(MiddlewareMixin):
    def process_request(self,request):
        paths = ['ttsx/index/','ttsx/login/','ttsx/register/',]
        for path in paths:
            if re.match(request.path,path):
                return None

        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect(reverse('ttsx:login'))
        user = TicketModel.objects.filter(ticket=ticket).first()

        if not user:
            return HttpResponseRedirect(reverse('ttsx:login'))

        if user.out_date.replace(tzinfo=None) < datetime.now():
            user.delete()
            return HttpResponseRedirect(reverse('ttsx:login'))

        request.user = user.user
