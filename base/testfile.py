from django.shortcuts import render
import json, os
from django.conf import settings
def load_alerts_from_file():
    json_path = os.path.join(settings.BASE_DIR, 'data', 'alerts_json.json')
    with open(json_path, 'r') as f:
        return json.load(f)
load_alerts_from_file()