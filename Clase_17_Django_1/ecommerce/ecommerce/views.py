# Respuestas con strings
from django.http import HttpResponse

# Renderizado de templates
from django.template import Template, Context, loader


from datetime import datetime

def say_hello(request):

    return HttpResponse("Hola mundo")


def say_hello_with_name(request, name):

    return HttpResponse(f"Hola {name}")

def print_add(request, num1, num2):

    return HttpResponse(f"{num1} + {num2} = {num1+num2}")

def index(request, nombre):

    # Paso 0: Crear un contexto
    datos_contexto = {"fecha_actual": datetime.now(), "username": nombre} 

    # Paso 1: Cargar contenido HTML 
    archivo = open(r"C:\Users\dev\Documents\coder40150\Clase_17_Django_1\ecommerce\ecommerce\templates\index.html", "r")
    contenido_html = archivo.read()
    archivo.close()

    # Paso 2: Crear la plantilla
    plantilla = Template(contenido_html)

    # Paso 3: Crear contexto
    contexto = Context(datos_contexto)

    # Paso 4: Preparar documento para renderizar 
    documento_a_renderizar = plantilla.render(contexto)

    # Paso 5: Devolver la respuesta al usuaio
    return HttpResponse(documento_a_renderizar)

def notas(request):

    # Paso 0: Crear el contexto
    datos = { "notas": [9,4,3,7,10, 8, 5, 10], "estudiante": "leonel" }

    # Paso 1: Cargar contenido HTML
    archivo = open(r"C:\Users\dev\Documents\coder40150\Clase_17_Django_1\ecommerce\ecommerce\templates\notas.html", "r")
    contenido = archivo.read()
    archivo.close()

    
    # Paso 2: Crear la plantilla
    plantilla = Template(contenido)

    # Paso 3: Crear le contexto
    contexto = Context(datos)

    # Paso 4: Renderizar el HTML con la informacion del contexto
    documento = plantilla.render(contexto)

    # Paso 5: Retornar el documento como respuesta
    return HttpResponse(documento)


def alumnos(request):
    
    datos = {"curso": "Python", "alumnos": ["Leonel", "Pedro", "Santi", "Maria", "Enrique"]}
    
    plantilla = loader.get_template("alumnos.html")

    documento = plantilla.render(datos)

    return HttpResponse(documento)
