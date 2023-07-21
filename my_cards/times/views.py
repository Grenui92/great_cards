from django.shortcuts import render, redirect
from django.views import View

from times.models import Sentences, Times
from times.management.commands.create_times_tables import verbs
class TimesView(View):
    template_name = 'times/times.html'

    def get(self, request):
        times = Times.objects.all()
        examples = {}
        for time in times:
            sentences = Sentences.objects.filter(time=time.id, owner=request.user.id)
            examples[time.name] = sentences
        print(verbs.values())
        return render(request, self.template_name, context={"times": zip(times, verbs.values()),
                                                            "examples": examples})
    
    def post(self, request, time_id):
        time = Times.objects.get(id=time_id)
        text = request.POST.get('sentence')
        Sentences.objects.create(text=text, owner=request.user, time=time)
        return redirect(to='times:times')
