import time
import uuid

from django.http import HttpResponse
from django.shortcuts import render

from .models import ValueItem


def sercat_items(request):
    value_items = ValueItem.objects.filter(level=1)
    context = {
        "value_items": value_items,
        "count": value_items.count()
    }
    return render(request, "base/sercat-items.html", context)


def create_test_data(request):
    start = time.perf_counter()
    for i in range(200):
        value_item = ValueItem(name=f"{uuid.uuid4()}", level=1)
        value_item.save()
        create_children(value_item)

    end = time.perf_counter()

    return HttpResponse(f"Done in {end - start} seconds")


def home(request):
    return render(request, "base/home.html")


def create_children(parent: ValueItem):
    if parent.level <= 6:
        for _ in range(2):
            child = ValueItem(name=f"{uuid.uuid4()}", level=parent.level + 1)
            child.save()
            parent.children.add(child)
            create_children(child)
