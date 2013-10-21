from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.shortcuts import render_to_response, redirect
from vote.models import Poll
from common.utils import is_brother
from django.contrib.auth.decorators import user_passes_test

from rush.models import Rushie


class VotingView(View):

    template_name = "vote/voting.html"

    def post(self, request, *args, **kwargs):
        if 'yes' in request.POST:
            rushee_id = request.POST['yes']
            vote = 'Y'

        if 'no' in request.POST:
            rushee_id = request.POST['no']
            vote = 'N'

        if rushee_id:
            p = Poll.objects.get(rushee_id=rushee_id)
            myVote, created = p.votes.get_or_create(brother=request.user.brother)
            myVote.vote = vote

            myVote.save()
            print myVote.vote

        return self.get(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):

        polls = Poll.objects.filter(open=True)

        polls_list = []

        for p in polls:
            vote = ''
            if p.votes.filter(brother=request.user.brother).exists():
                poll_vote = p.votes.get(brother=request.user.brother)
                vote = poll_vote.vote
            polls_list.append((p,vote))

        context = {
            'polls': polls_list,
        }

        return render_to_response(self.template_name, context, context_instance=RequestContext(request))

    @method_decorator(user_passes_test(is_brother))
    def dispatch(self, request, *args, **kwargs):
        return super(VotingView, self).dispatch(request, *args, **kwargs)

