from django.shortcuts import redirect, render
import json, os
from django.conf import settings
from .models import Message

def intro(request):
    return render(request, "base/intro.html")

# Load alerts from JSON
def load_alerts_from_file():
    json_path = os.path.join(settings.BASE_DIR, 'data', 'alerts_json.json')
    with open(json_path, 'r') as f:
        return json.load(f)

def home(request):
    alerts = load_alerts_from_file()
    context = {'alertings': alerts}
    return render(request, "base/home.html", context)

def alerts(request, pk):
    alerts = load_alerts_from_file()
    alert = next((a for a in alerts if str(a['id']) == pk), None)
    
    messages = Message.objects.filter(alert_id=pk).order_by('-timestamp')

    if request.method == "POST":
        username = request.POST.get('username', 'Anonymous')
        content = request.POST.get('content')
        if content:
            Message.objects.create(alert_id=pk, username=username, content=content)
            return redirect(f'/alerts/{pk}/')

    context = {'alert': alert, 'messages': messages}
    return render(request, "base/alerts.html", context)


