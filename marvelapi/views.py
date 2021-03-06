from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
import requests
from django.http import JsonResponse
import hashlib
import time
from marvelapi.models import Rus
from marvelapi.config import private_key, public_key
from rest_framework.decorators import api_view


ts = str(time.time())
m = hashlib.md5((ts+private_key+public_key).encode('utf-8')).hexdigest()


@api_view(['GET'])
def show_films(request):
    response = requests.get(f'http://gateway.marvel.com/v1/public/comics?ts={ts}&apikey={public_key}&hash={m}')
    result = response.json()
    data = []
    for title in result['data']['results']:
        data.append(title['title'])
    for i in range(len(data)):
        try:
            tmp = Rus.objects.get(eng_title=data[i])
            data[i] = (data[i], tmp.rus_title)
        except ObjectDoesNotExist:
            data[i] = (data[i], 'Rus_name does not exist')
    return JsonResponse({'result': data}, json_dumps_params={'ensure_ascii':False})


@api_view(['GET'])
def local_comic_names(request):
    return JsonResponse({'result': list(Rus.objects.values('eng_title','rus_title'))}, json_dumps_params={'ensure_ascii':False})
