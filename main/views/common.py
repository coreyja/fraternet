# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.views.generic import DetailView, UpdateView, TemplateView
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

from main.models import Profile, Brother
from main.forms import BrotherForm
from rush.models import Rushie
from rush.forms import RushieEditForm

def dashboard_view(request):
    return redirect('calendar_view')

    # if request.user.is_authenticated():
    #     return render_to_response('dashboard.html', context_instance=RequestContext(request))
    # else:
    #     return render_to_response('static/landing.html', context_instance=RequestContext(request))


class ProfileView(DetailView):
    template_name = 'profile/detail.html'
    model = Profile

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if hasattr(self.request.user, 'brother'):
            self.model = Brother
        elif hasattr(self.request.user, 'rushie'):
            self.model = Rushie

        return super(ProfileView, self).dispatch(*args, **kwargs)

    def get_object(self, queryset=None):
        return self.model.objects.get(id=self.request.user.id)


class ProfileEditView(UpdateView):
    template_name = 'profile/edit.html'
    form_class = BrotherForm
    model = Profile

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if hasattr(self.request.user, 'brother'):
            self.model = Brother
        elif hasattr(self.request.user, 'rushie'):
            self.model = Rushie
            self.form_class = RushieEditForm

        return super(ProfileEditView, self).dispatch(*args, **kwargs)

    def get_object(self, queryset=None):
        return self.model.objects.get(id=self.request.user.id)

    def get_success_url(self):
        return reverse('profile')


class GeneralInfoView(TemplateView):
    template_name = 'static/general_info.html'

class ContactUsView(TemplateView):
    template_name = 'static/contact.html'


