from django.views.generic import DetailView, UpdateView, CreateView, DeleteView, ListView, FormView
from django.shortcuts import render_to_response, redirect
from django.core.exceptions import PermissionDenied

from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator


from main.models import Brother
from main.forms import BrotherForm, BrotherCreateForm

import logging
logger = logging.getLogger(__name__)


class BrotherCreateView(FormView):
    template_name = 'brother/create.html'
    form_class = BrotherCreateForm
    success_url = '/'

    @method_decorator(permission_required('main.add_brother'))
    def dispatch(self, *args, **kwargs):
        return super(BrotherCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']

        phone = form.cleaned_data['phone']
        grad_year = form.cleaned_data['grad_year']

        majors = form.cleaned_data['majors']

        bro = Brother.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            grad_year=grad_year,
        )

        bro.majors = majors
        bro.save()

        return redirect('admin')


class BrotherListView(ListView):
    model = Brother
    template_name = 'brother/list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BrotherListView, self).dispatch(*args, **kwargs)

class BrotherDetailView(DetailView):
    model = Brother
    template_name = 'brother/detail.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(BrotherDetailView, self).dispatch(*args, **kwargs)

    def get_object(self, queryset=None):
        return Brother.objects.get(username=self.kwargs['username'])

class BrotherEditView(UpdateView):
    model = Brother
    template_name = 'brother/edit.html'
    form_class = BrotherForm
    success_url = '/'

    def get_object(self, queryset=None):
        bro = Brother.objects.get(username=self.kwargs['username'])

        if self.request.user.brother.can_edit_brother(bro.id):
            return bro

        raise PermissionDenied