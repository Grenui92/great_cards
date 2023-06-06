from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from chat.services.conversation import text_generator

@csrf_exempt
def chat(request, messages = []):
    if request.method == "POST":
        if len(messages) >= 20:
            messages = messages[1:]
        message = request.POST.get("message", "")

        messages.append({"role": "system",
                         "content": "Show linguistic mistakes in user message."
                                    "Tell about mistakes in message."
                                    "Then answer user request."})
        messages.append({"role": "user", "content": message})

        response_role, response_content = text_generator(messages)
        messages.append({"role": response_role, "content": response_content})
        print(len(messages))
        for k in messages:
            print(k)
        return JsonResponse({'response': f'YOU: {message.strip()}<br>'
                                         f'{response_role.upper()}: {response_content.strip()}<br><br>'})
    if request.method == 'GET':
        messages = []
        return render(request, 'chat/chat_ai.html')
