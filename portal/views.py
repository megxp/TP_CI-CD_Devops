import sentry_sdk
from django.shortcuts import render

def home(request):
    return render(request, 'portal/index.html')

def trigger_error(request):
    try:
        1 / 0
    except Exception as e:
        sentry_sdk.capture_exception(e)

    return render(request, 'portal/index.html', {'error': True})