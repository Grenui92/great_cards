from django.views.generic import View
from django.shortcuts import render


class NewsListView(View):
    template_name = 'news/index.html'

    def get(self, request):
        video = 'Hi, my dear friends!'
        return render(request, self.template_name, context={'video': video})
