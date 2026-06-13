from django.http import HttpResponse

def sentry_test(request):
    1 / 0
    return HttpResponse("ok")
