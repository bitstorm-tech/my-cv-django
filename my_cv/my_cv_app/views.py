from django.shortcuts import render


def handle(request):
    return render(request, 'base/base.html')
