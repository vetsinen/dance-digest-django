from django.shortcuts import render
from .repository import fetch

def index(request):
    e = fetch('w2>=0')
    return render(request, 'digest/first.html', {'title':'42', 'events':e})


def event(request, id):
    print(id)
    return render(request, 'digest/event-details.html',{'descr':'long description'})