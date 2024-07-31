from ..models import Sotrudniki
import json


class ValidateExeption(Exception):
    pass

def get(Id=0):
    if Id==0:
        return Sotrudniki.objects.all()
    gen  = Sotrudniki.objects.get(id = Id)
    return gen

def Serialise(Sotrudniki):
    return "{"+f"id:{Sotrudniki.id} , name:{Sotrudniki.name}"+"}"

def SerialiseList(Sotrudnikis):
    jsonResult = "["
    for g in Sotrudnikis:
        jsonResult+=Serialise(g)+","
    jsonResult+="]"
    return jsonResult

def Desirialise(JsonSotrudniki):
    Sotrudniki = Sotrudniki()
    
    Sotrudniki.name = json.loads(JsonSotrudniki.decode())['name']

    return Sotrudniki

def Validate(Sotrudniki):
    if len(Sotrudniki.name) >50:
        raise ValidateExeption()

def post(JsonSotrudniki):
    entity = Desirialise(JsonSotrudniki)
    Validate(entity)
    entity.save()
    return entity

def update(JsonSotrudniki,Id):
    entity = Desirialise(JsonSotrudniki)
    Validate(entity)
    gen = Sotrudniki.objects.get(id = Id)
    gen.name = entity.name
    gen.save()

def delete(Id):
    gen = Sotrudniki.objects.get(id=Id)
    gen.delete()

def search(query):
    _id = query.get("id",0)
    filt = Sotrudniki.objects.all()
    if _id>0 :
        filt = filt.filter(id = _id)
    _name = query.get("name","")
    if _name!= "":
        filt = filt.filter(name = _name)
    return SerialiseList(filt)
    