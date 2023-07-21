from django.shortcuts import render, redirect
from django.views import View

from times.models import Sentences, Times

class TimesView(View):
    template_name = 'times/times.html'

    def get(self, request):
        times = Times.objects.all()
        result = []
        for time in times:
            result.append(Sentences.objects.filter(time=time.id, owner=request.user.id))
        return render(request, self.template_name)