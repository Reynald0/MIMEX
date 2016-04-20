# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect

def inicio(request):
	return render(request, 'inicio.html') #Agarra la ruta plantillas/inicio.html

def informacion(request):
	return render(request, 'informacion.html')

def miel(request):
	return render(request, 'miel.html')

def contacto(request):
	return render(request, 'contacto.html')