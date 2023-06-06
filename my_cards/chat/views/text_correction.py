from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from chat.services.checking_sentences import text_generator


@csrf_exempt
def text_correction(request):
    if request.method == 'POST':
        message = request.POST.get('message')

        chatbot_response = text_generator(message)
        for k in chatbot_response:
            print(k)
        return JsonResponse({'response': f'Original: {message}\n'
                                         f'Correct: {chatbot_response.strip()}'})

    return render(request, 'chat/text_correction.html')