# Respuestas con strings
from django.http import HttpResponse

# Renderizado de templates
from django.template import Template, Context


def say_hello(request):

    return HttpResponse("Hola mundo")


def say_hello_with_name(request, name):

    return HttpResponse(f"Hola {name}")

def print_add(request, num1, num2):

    return HttpResponse(f"{num1} + {num2} = {num1+num2}")

def index(request, name):

    # Paso 1: Cargar contenido HTML 
    archivo = open(r"C:\Users\dev\Documents\coder-40150\django1\ecommerce\ecommerce\templates\index.html", "r")
    contenido_html = archivo.read()
    archivo.close()

    # Paso 2: Crear la plantilla
    plantilla = Template(contenido_html)

    # Paso 3: Crear contexto
    contexto = Context({"nombre": name})

    # Paso 4: Preparar documento para renderizar 
    documento_a_renderizar = plantilla.render(contexto)

    # Paso 5: Devolver la respuesta al usuaio
    return HttpResponse(documento_a_renderizar)