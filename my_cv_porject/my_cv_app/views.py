from django.http import HttpResponse


def handle(request):
    return HttpResponse('Yup, works as intended!')
