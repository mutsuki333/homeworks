from django.urls import path, re_path
from django.http import JsonResponse, HttpResponse
import json

from home.models import Item


def msg(request):
    return JsonResponse({'foo':'bar'})

def newItem(request):
    data = json.loads(request.body.decode("utf-8"))
    try:
        name = data['name']
        description = data['description']
        stock = data['stock']
    except:
        return HttpResponse(status=404)
    try:
        item = Item.objects.get(name=data['name'])
    except:
        item = Item(name=name,
                    description=description,
                    stock=stock)
        item.save()
        return HttpResponse(item.id)
    item.description = description
    item.stock = stock
    item.save()
    return HttpResponse(item.id)

def setPic(request):
    id = request.GET.get('id')
    try:
        item = Item.objects.get(id=id)
    except:
        return HttpResponse(status=404)
    try:
        if item.picture:
            item.picture.delete()
        setattr(item,'picture',request.FILES['file'])
        item.save()
    except:
        print('failed')
        return HttpResponse('failed')
    return HttpResponse('success')

def getItem(request):
    id = request.GET.get('id')
    try:
        item = Item.objects.filter(id=id).values()
    except:
        return HttpResponse(status=404)
    return JsonResponse(list(item),safe=False)

def getItems(request):
    try:
        items = Item.objects.all().values()
    except:
        return HttpResponse(status=404)
    return JsonResponse(list(items),safe=False)

def delItem(request):
    id = request.GET.get('id')
    try:
        item = Item.objects.get(id=id)
    except:
        return HttpResponse(status=404)
    if item.picture:
        item.picture.delete()
    item.delete()
    return HttpResponse('ok')

def inc(request):
    id = request.GET.get('id')
    try:
        item = Item.objects.get(id=id)
    except:
        return HttpResponse(status=404)
    item.stock += 1
    item.save()
    return HttpResponse('ok')

def dec(request):
    id = request.GET.get('id')
    try:
        item = Item.objects.get(id=id)
    except:
        return HttpResponse(status=404)
    item.stock -= 1
    item.save()
    return HttpResponse('ok')


urlpatterns = [
    path('msg', msg),
    path('new_item',newItem),
    path('set_pic',setPic),
    path('get_item',getItem),
    path('del_item',delItem),
    path('get_items',getItems),
    path('inc',inc),
    path('dec',dec)
]