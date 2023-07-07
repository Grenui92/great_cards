from django.shortcuts import render

def room(request, message = 'Hi, my dear'):
    return render(request, 'chat/chat.html', context={'room_name': message})