from django.shortcuts import render, redirect
from django.views import View

class TimesView(View):
    template_name = 'times/times.html'

    def get(self, request):
        return render(request, self.template_name)