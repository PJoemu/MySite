# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def home(request):
    return render_to_response('index.html')


def portal(request):
    return render_to_response('portal.html')
