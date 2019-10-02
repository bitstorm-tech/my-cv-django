import time
import uuid

from django.http import HttpResponse
from django.shortcuts import render

from .models import ValueItem


def handle(request):
    context = {
        "value_items": ValueItem.objects.filter(level=1),
        "count": ValueItem.objects.count()
    }
    return render(request, 'base/base.html', context)


def create_test_data(request):
    start = time.perf_counter()
    for i in range(1):
        value_item = ValueItem(name=f"{uuid.uuid4()}", level=1)
        value_item.save()
        create_children(value_item)

    end = time.perf_counter()

    return HttpResponse(f"Done in {end - start}")


def create_children(parent: ValueItem):
    if parent.level <= 4:
        for i in range(parent.level + 1):
            print(f"Level: {parent.level}")
            child = ValueItem(name=f"{uuid.uuid4()}", level=parent.level + 1)
            print(f"Append child: {child}")
            # child.save()
            # parent.children.add(child)
            # create_children(child)
