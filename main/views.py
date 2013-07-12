# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

def dashboard_view(request):
    if request.user.is_authenticated():
        return render_to_response('dashboard.html', context_instance=RequestContext(request))
    else:
        return render_to_response('static/landing.html', context_instance=RequestContext(request))
