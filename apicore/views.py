from django.http import HttpResponseRedirect
from django.shortcuts import render


def redirect_view(request):
    return HttpResponseRedirect(redirect_to='https://developer.anuragdhadse.com')
