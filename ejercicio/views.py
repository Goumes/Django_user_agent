from django.shortcuts import render
from django_user_agents.utils import get_user_agent


def index(request):
    return render(request, 'ejercicio/index.html', {})


def info(request):
    user_agent = get_user_agent(request)
    data = ""
    host = user_agent.device
    ip = user_agent.get_browser()
    if user_agent.is_mobile:
        data = "Hola, estas usando un móvil"
    elif user_agent.is_tablet:
        data = "Hola, estas usando una tablet"
    elif user_agent.is_pc:
        data = "Hola, estas usando un pc"
    elif user_agent.is_bot:
        data = "Hola, estas usando un bot"
    elif user_agent.is_touch_capable:
        data = "Estas desde un dispositivo táctil"

    return render(request, 'ejercicio/info.html', {'data': data, 'host': host, 'ip': ip, 'user_agent': user_agent})

def about_me(request):
    user_agent = get_user_agent(request)
    data = ""
    host = request.META.get("REMOTE_HOST")
    ip = request.META.get('REMOTE_ADDR')
    tactil = "El dispositivo no es táctil"

    if user_agent.is_mobile:
        data = "Hola, estas usando un móvil"
    elif user_agent.is_tablet:
        data = "Hola, estas usando una tablet"
    elif user_agent.is_pc:
        data = "Hola, estas usando un pc"
    elif user_agent.is_bot:
        data = "Hola, estas usando un bot"
    elif user_agent.is_touch_capable:
        tactil = "Estas desde un dispositivo táctil"

    return render(request, 'ejercicio/about_me.html', {'data': data, 'host': host, 'ip': ip, 'tactil': tactil})
