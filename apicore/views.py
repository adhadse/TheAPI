from django.http import HttpResponseRedirect


def redirect_view(request):
    return HttpResponseRedirect(redirect_to='https://developer.anuragdhadse.com')
