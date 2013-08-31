from django.views.generic import DetailView, UpdateView, CreateView, DeleteView, ListView, FormView
from django.shortcuts import render_to_response, redirect
from django.core.exceptions import PermissionDenied

from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.utils.decorators import method_decorator

from rush.models import Rushie
from rush.forms import RushieCreateForm
from common.utils import is_brother


class RushieCreateView(FormView):
    form_class = RushieCreateForm
    template_name = 'rushie/create.html'
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']

        phone = form.cleaned_data['phone']
        grad_year = form.cleaned_data['grad_year']

        majors = form.cleaned_data['majors']

        rushie = Rushie.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            grad_year=grad_year,
        )

        rushie.majors = majors
        rushie.save()

        return redirect('dashboard')


class RushieListView(ListView):
    model = Rushie
    template_name = 'rushie/list.html'

    @method_decorator(user_passes_test(is_brother))
    def dispatch(self, request, *args, **kwargs):
        return super(RushieListView, self).dispatch(request, *args, **kwargs)

class RushieDetailView(DetailView):
    model = Rushie
    template_name = 'rushie/detail.html'

    @method_decorator(user_passes_test(is_brother))
    def dispatch(self, request, *args, **kwargs):
        return super(RushieDetailView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return Rushie.objects.get(username=self.kwargs['username'])