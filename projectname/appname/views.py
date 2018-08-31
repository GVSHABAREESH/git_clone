# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from appname.models import classname
from appname.serializers import classnameSerializer

# Create your views here.
def htmlfile(request):
    obj = classname.objects.all()
    return render(request,'htmlfile.html',{'obj':obj})

