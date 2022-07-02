from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from time import sleep
from random import randint

from django.conf import settings
import statsd
stats = statsd.StatsClient(settings.STATSD_HOST, settings.STATSD_PORT)

@csrf_exempt
def hello_world(request):
    n = randint(0,100)
    step = 0.005
    stats.gauge("parameter", n , tags={'view':'hello_world'})
    wait = n*step 
    sleep(wait)
    return JsonResponse({'msg':'Hello World!', 'took': f'{wait:2f} seconds'})
