# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response


@login_required(login_url='/login/')
def portal(request):
    return render_to_response('portal.html')
