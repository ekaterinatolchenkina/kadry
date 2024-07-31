from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseNotFound,JsonResponse,HttpResponseServerError
from django.urls import path
from ..ServiceKadri import serviceZarplata
from ..models import Zarplata
from django.core import serializers

def _index(request):
    if request.method =="GET":
       return  HttpResponse(serializers.serialize("json",_getAll(request)))
    if request.method == "POST":
        return HttpResponse(_post(request))
    return HttpResponseBadRequest("Bad Request")

def _getAll(request):
    return serviceZarplata.get()

def _post(request):
    try:
        res = serviceZarplata.post(request.body)
        return HttpResponse(res)
    except serviceZarplata.ValidateExeption:
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
    except Zarplata.DoesNotExist:
        return HttpResponseNotFound("Такой зп нет")
    except:
        return HttpResponseServerError() 



def _get(request,Id):    
        return serviceZarplata.get(Id)
   

def _put(request,Id):
    if not Id>0:
        return HttpResponseBadRequest("Bad Request")
    try:
        return HttpResponse(serviceZarplata.update(request.body,Id))
    except Zarplata.DoesNotExist:
        return HttpResponseNotFound()
    except:
        return HttpResponseServerError()

def _del(request,Id):
    try:
        serviceZarplata.delete(Id)
        return HttpResponse()
    except Zarplata.DoesNotExist:
        return HttpResponseNotFound()
    except:
        return HttpResponseServerError()

def _search(request):
    try:
        return HttpResponse(serviceZarplata.search(request.GET))
    except Zarplata.DoesNotExist:
        return HttpResponseNotFound()
    except:
        return HttpResponseServerError()


route_toKadriZarplata = [
    path("", _index),
    path("<int:Id>", _indexId),
    path("search", _search),
]