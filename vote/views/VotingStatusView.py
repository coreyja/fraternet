from django.utils.decorators import method_decorator
from django.views.generic import View
from django.shortcuts import render_to_response, redirect
from vote.models import Poll
from common.utils import is_brother
from django.contrib.auth.decorators import user_passes_test

from rush.models import Rushie


class VotingStatusView(View):

    template_name = "vote/status.html"

    def get(self, request, *args, **kwargs):

        polls = Poll.objects.filter(open=True)

        context = {
            'polls': polls,
        }

        return render_to_response(self.template_name, context)

    def post(self, request, *args, **kwargs):
        if 'create' in request.POST:
            rushee_id = request.POST['create']
            rushee = Rushie.objects.get(id=rushee_id)

            Poll.objects.create(rushee=rushee)

        if 'close' in request.POST:
            rushee_id = request.POST['close']

            Poll.objects.filter(rushee_id=rushee).update(open=False)

        if 'clear' in request.POST:
            rushee_id = request.POST['clear']

            p = Poll.objects.get(rushee_id=rushee)
            p.votes.clear()

        return self.get(request, *args, **kwargs)

    @method_decorator(user_passes_test(is_brother))
    def dispatch(self, request, *args, **kwargs):
        return super(VotingStatusView, self).dispatch(request, *args, **kwargs)

