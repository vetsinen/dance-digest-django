from django.shortcuts import render

def index(request):
    return render(request, 'digest/first.html', {"title":'Dance Digest'})