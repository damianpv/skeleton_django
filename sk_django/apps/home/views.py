# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
#from django.http import HttpResponseRedirect, HttpResponse

#from django.utils.timezone import utc
#from datetime import datetime
#from django.conf import settings
#from django.contrib.auth import login, logout, authenticate
#from django.http import HttpResponseRedirect
#from django.contrib.auth.models import User

import django

def home_view(request):

    ctx = {
        'dj_version': django.get_version(),
    }
    response = render_to_response('home/index.html', ctx, context_instance=RequestContext(request))
    return response