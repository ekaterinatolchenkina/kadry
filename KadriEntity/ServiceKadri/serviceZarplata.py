from ..models import Zarplata
import json


class ValidateExeption(Exception):
    pass

def get(Id=0):
    if Id==0:
        return Zarplata.objects.all()
    gen  = Zarplata.objects.get(id = Id)
    return gen

def Serialise(Zarplata):
    return "{"+f"id:{Zarplata.id} , name:{Zarplata.name}"+"}"

def SerialiseList(Zarplatas):
    jsonResult = "["
    for g in Zarplatas:
        jsonResult+=Serialise(g)+","
    jsonResult+="]"
    return jsonResult

def Desirialise(JsonZarplata):
    Zarplata = Zarplata()
    
    Zarplata.name = json.loads(JsonZarplata.decode())['name']

    return Zarplata

def Validate(Zarplata):
    if len(Zarplata.name) >50:
        raise ValidateExeption()

def post(JsonZarplata):
    entity = Desirialise(JsonZarplata)
    Validate(entity)
    entity.save()
    return entity

def update(JsonZarplata,Id):
    entity = Desirialise(JsonZarplata)
    Validate(entity)
    gen = Zarplata.objects.get(id = Id)
    gen.name = entity.name
    gen.save()

def delete(Id):
    gen = Zarplata.objects.get(id=Id)
    gen.delete()

def search(query):
    _id = query.get("id",0)
    filt = Zarplata.objects.all()
    if _id>0 :
        filt = filt.filter(id = _id)
    _name = query.get("name","")
    if _name!= "":
        filt = filt.filter(name = _name)
    return SerialiseList(filt)
    