from django.shortcuts import render
from .repository import fetch, fetch_by_id
import datetime

def index(request):
    weekday = datetime.datetime.today().weekday()

    e = fetch(f'w2>={weekday}')
    return render(request, 'digest/first.html', {'title':'42', 'events':e})


def event(request, id):
    print(id)
    event = fetch_by_id(id)
    url = event['pic'][0]['url'] if event['pic'] else None
    return render(request, 'digest/event-details.html',{'e': event, 'url': url })