from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import permission_required
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView, ListView, FormView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect
from main.models import Brother
from main.forms import BrotherForm

@permission_required('brother.is_admin', raise_exception=True)
def admin_view(request):
    return render_to_response('admin/admin.html', context_instance=RequestContext(request))
