from django.http import HttpResponse,  JsonResponse
from django.template import Template, Context
from django.shortcuts import render
from django.shortcuts import redirect
import os
from modelo import models

def validar_registro_maestro(maestro):
    if maestro.nombre == '':
        return False
    if maestro.direccion == '':
        return False
    if maestro.telefono == '':
        return False
    return True

def validar_registro_alumno(alumno):
    if alumno.nombre == '':
        return False
    if alumno.direccion == '':
        return False
    if alumno.salon == '':
        return False
    if alumno.maestro_id == '':
        return False
    return True


def registro_Maestros(request):
    if request.method == 'GET':
        template = 'registroMaestros.html'
        return render(request, template)
    elif request.method == 'POST':
        nombre = request.POST.get('nombre','')
        direccion = request.POST.get('direccion','')
        telefono = request.POST.get('telefono','')

        maestro = models.Maestro()
        maestro.nombre = nombre
        maestro.direccion = direccion
        maestro.telefono = telefono

        if validar_registro_maestro(maestro):
            maestro.save()
            return redirect('/RegistroMaestros')

        else:
            template = 'registroMaestros.html'
            contexto = {'Errores': 'Algunos campos están vacios'}
            return render(request, template, contexto)


def registro_Alumnos(request):
    if request.method == 'GET':
        template = 'registroAlumnos.html'
        maestros = models.Maestro.objects.all()
        contexto = {'maestros': maestros}
        return render(request, template, contexto)
    elif request.method == 'POST':
        nombre = request.POST.get('nombre','')
        direccion = request.POST.get('direccion','')
        maestro = request.POST.get('maestro','')
        salon = request.POST.get('salon','')

        alumno = models.Alumno()
        alumno.nombre = nombre
        alumno.direccion = direccion
        alumno.salon = salon
        alumno.maestro_id = maestro

        if validar_registro_alumno(alumno):
            alumno.save()
            return redirect('/RegistroAlumnos')


        else:
            template = 'registroAlumnos.html'
            contexto = {'Errores': 'Algunos campos están vacios'}
            return render(request, template, contexto)
