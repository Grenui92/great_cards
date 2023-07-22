from django.shortcuts import render, redirect
from django.views import View

from times.models import Sentences, Times
from tools.decorators import class_login_required


class TimesView(View):
    template_name = 'times/times.html'

    @class_login_required
    def get(self, request):
        times = Times.objects.all()
        examples = {}
        for time in times:
            sentences = Sentences.objects.filter(time=time.id, owner=request.user.id)
            examples[time.name] = sentences

        return render(request, self.template_name, context={"times": times,
                                                            "examples": examples})
    @class_login_required
    def post(self, request, time_id):
        time = Times.objects.get(id=time_id)
        text = request.POST.get('sentence')
        if text:
            Sentences.objects.create(text=text, owner=request.user, time=time)
        return redirect(to='times:times')

class DeleteSentenceView(View):
    
    @class_login_required
    def post(self, request, sentence_id):
        Sentences.objects.get(id=sentence_id).delete()
        return redirect(to='times:times')