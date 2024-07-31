from ..models import Dolznosty
import json


class ValidateExeption(Exception):
    pass

def get(Id=0):
    if Id==0:
        return Dolznosty.objects.all()
    gen  = Dolznosty.objects.get(id = Id)
    return gen

def Serialise(Dolznosty):
    return "{"+f"id:{Dolznosty.id} , name:{Dolznosty.name}"+"}"

def SerialiseList(Dolznostys):
    jsonResult = "["
    for g in Dolznostys:
        jsonResult+=Serialise(g)+","
    jsonResult+="]"
    return jsonResult

def Desirialise(JsonDolznosty):
    Dolznostys = Dolznostys()
    
    Dolznostys.name = json.loads(JsonDolznosty.decode())['name']

    return Dolznostys

def Validate(Dolznostys):
    if len(Dolznostys.name) >50:
        raise ValidateExeption()

def post(JsonDolznosty):
    entity = Desirialise(JsonDolznosty)
    Validate(entity)
    entity.save()
    return entity

def update(JsonDolznosty,Id):
    entity = Desirialise(JsonDolznosty)
    Validate(entity)
    gen = Dolznosty.objects.get(id = Id)
    gen.name = entity.name
    gen.save()

def delete(Id):
    gen = Dolznosty.objects.get(id=Id)
    gen.delete()

def search(query):
    _id = query.get("id",0)
    filt = Dolznosty.objects.all()
    if _id>0 :
        filt = filt.filter(id = _id)
    _name = query.get("name","")
    if _name!= "":
        filt = filt.filter(name = _name)
    return SerialiseList(filt)
    