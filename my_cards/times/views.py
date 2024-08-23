from django.shortcuts import render, redirect
from django.views import View

from times.models import Sentences, Times
from tools.decorators import class_login_required


class TimesView(View):
    """A class-based view for handling times-related functionality.
    Attributes:
        template_name (str): The name of the template to be rendered.
    """

    template_name = 'times/times.html'

    @class_login_required
    def get(self, request):
        """Return the times page. Get all times from the database and all
        sentences for each time. Render the times page with the times and
        sentences.

        :param request: request object
        :return: render
        """
        times = Times.objects.all()
        examples = {}
        for time in times:
            sentences = Sentences.objects.filter(
                time=time.id, owner=request.user.id)
            examples[time.name] = sentences

        return render(request,
                      self.template_name,
                      context={"times": times,
                               "examples": examples})

    @class_login_required
    def post(self, request, time_id):
        """Get the sentence from the form and create a new sentence in the
        database.

        :param request: request object
        :param time_id: The id of the Time
        :return: redirect
        """
        time = Times.objects.get(id=time_id)
        text = request.POST.get('sentence')
        if text:
            Sentences.objects.create(text=text, owner=request.user, time=time)
        return redirect(to='times:times')


class DeleteSentenceView(View):
    """A class-based view for handling the deletion of sentences."""

    @class_login_required
    def post(self, request, sentence_id):
        """Delete the sentence from the database.

        :param request: request object
        :param sentence_id: The id of the sentence to be deleted
        :return: redirect
        """
        Sentences.objects.get(id=sentence_id).delete()
        return redirect(to='times:times')
