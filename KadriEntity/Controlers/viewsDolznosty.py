from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseNotFound,JsonResponse,HttpResponseServerError
from django.urls import path
from ..ServiceKadri import serviceDolznosty
from ..models import Dolznosty
from django.core import serializers

def _index(request):
    if request.method =="GET":
       return  HttpResponse(_getAll(request))
       
    if request.method == "POST":
        return HttpResponse(_post(request))
    return HttpResponseBadRequest("Bad Request")

def _getAll(request):
    return serviceDolznosty.get()

def _post(request):
    try:
        res = serviceDolznosty.post(request.body)
        return HttpResponse(res)
    except serviceDolznosty.ValidateExeption:
        return HttpResponseBadRequest("Validate Eror")    
    except:
        return HttpResponseServerError()

def _indexId(request,Id):
    try:
        if not Id >0:
            return HttpResponseBadRequest("Bad Request id not valid")
        if request.method =="GET":
            return  JsonResponse(_get(request,Id))
        if request.method == "PUT":
            return JsonResponse(_put(request,Id))
        if request.method == "DELETE":
            return HttpResponse(_del(request,Id))
        return HttpResponseBadRequest("Bad Request") 
    except Dolznosty.DoesNotExist:
        return HttpResponseNotFound("Такой должности нет")
    except:
        return HttpResponseServerError() 



def _get(request,Id):    
        return serviceDolznosty.get(Id)
   

def _put(request,Id):
    if not Id>0:
        return HttpResponseBadRequest("Bad Request")
    try:
        return HttpResponse(serviceDolznosty.update(request.body,Id))
    except Dolznosty.DoesNotExist:
        return HttpResponseNotFound()
    except:
        return HttpResponseServerError()

def _del(request,Id):
    try:
        serviceDolznosty.delete(Id)
        return HttpResponse()
    except Dolznosty.DoesNotExist:
        return HttpResponseNotFound()
    except:
        return HttpResponseServerError()

def _search(request):
    try:
        return HttpResponse(serviceDolznosty.search(request.GET))
    except Dolznosty.DoesNotExist:
        return HttpResponseNotFound()
    except:
        return HttpResponseServerError()


route_toKadriDolznosty = [
    path("", _index),
    path("<int:Id>", _indexId),
    path("search", _search),
]