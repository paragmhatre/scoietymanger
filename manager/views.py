from django.shortcuts import render
from django.shortcuts import render_to_response


# Create your views here.
def login_view(request):
    return render_to_response('login.html')


def setup_view(request):
    return render_to_response('setup.html')


def add_sabhasad_view(request):
    return render_to_response('add_sabhasad.html')


def pavti_pushtak(request):
    return render_to_response('pavti_pushtak.html')

def menu(request):
    return render_to_response('menu.html')
