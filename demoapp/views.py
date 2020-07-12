from django.http import HttpResponse


def hello(request):


    return HttpResponse("<h2> Welcome to Django <h2>")
