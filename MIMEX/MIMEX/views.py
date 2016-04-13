# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect

def inicio(request):
	return render(request, 'inicio.html') #Agarra la ruta plantillas/inicio.html