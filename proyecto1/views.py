from django import template
from django.http import HttpResponse #importar 
import datetime
from django.template import Template,Context
from django.template import loader
from django.shortcuts import render
def saludo(request):    # primera vista
    
    temas1=["juan","andres","pepito","dany"]
    nombre="jose"
    apellido="parra"
    fecha_actual1=datetime.datetime.now()
    #doc_externo=open("C:/Users/jose/Documents/proyectosdjango/proyecto1/proyecto1/plantilla1/plantillaluis.html")
    #plt=Template(doc_externo.read()) 
    #doc_externo.close()
    #doc_externo=loader.get_template("plantillaluis.html")
    #ctx=Context({"nombre_persona":nombre,"apellido_persona":apellido,"h_actual":fecha_actual1, "temas":temas1})
    #documento=doc_externo.render({"nombre_persona":nombre,"apellido_persona":apellido,"h_actual":fecha_actual1, "temas":temas1})
    #return HttpResponse(documento)
    return render(request, "plantillaluis.html",{"nombre_persona":nombre,"apellido_persona":apellido,"h_actual":fecha_actual1, "temas":temas1})
    
def fecha(request):
    fecha_actual=datetime.datetime.now()
    mostrar="<html><body><h1>fecha actual %s </h1></body></html>"%fecha_actual
    return HttpResponse(mostrar)
def calculaedad(request,edad,agno):
    #edadactual=18
    periodo=agno-2019
    edadfutura=edad+periodo
    fecha_actual=datetime.datetime.now()
    mostrar1="<html><body><h1>en el año %s tendras %s años </h1></body></html>"%(agno,edadfutura)
    return HttpResponse(mostrar1)
def cursoc(request):
    fecha_actual=datetime.datetime.now()
    return render(request,"cursoc.html",{"damefecha":fecha_actual})
def matematicas(request):
    fecha_actual=datetime.datetime.now()
    return render(request,"matematicas.html",{"damefecha":fecha_actual})