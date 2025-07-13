from django.shortcuts import render
from django.http import JsonResponse
from .models import Item

def items_list(request):
    items = Item.objects.all()
    data = [{"id": item.id, "name": item.name, "description": item.description} for item in items]
    return JsonResponse(data, safe=False)
