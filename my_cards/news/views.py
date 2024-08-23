from django.views.generic import View
from django.shortcuts import render


class NewsListView(View):
    """News list view."""

    template_name = 'news/index.html'

    def get(self, request):
        """Return the news list page.

        :param request: request object
        :return: render
        """
        message = 'Hi, my dear friends!'
        return render(request, self.template_name, context={'video': message})
