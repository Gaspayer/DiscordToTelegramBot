from django.shortcuts import render
from .forwarder import enable_forwarding, disable_forwarding
from . import forwarder  # import the module so that we can access its global variables

def index(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'enable':
            enable_forwarding()
        elif action == 'disable':
            disable_forwarding()
    status = str(forwarder.bot_name)+'  Running, forwarding to '+forwarder.TELEGRAM_CHAT_ID if forwarder.forward_enabled else str(forwarder.bot_name)+'  Stopped'
    return render(request, 'forwarder_app/index.html', {'status': status})
