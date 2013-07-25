from django.views.generic import DetailView, UpdateView, CreateView, DeleteView, ListView, FormView
from django.shortcuts import render_to_response, redirect

from main.models import Brother
from main.forms import BrotherForm

class BrotherCreateView(FormView):
    template_name = 'admin/add_brother.html'
    form_class = BrotherForm
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']

        Brother.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)

        return redirect('admin')