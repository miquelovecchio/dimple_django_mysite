from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context



def hello_world(request):
	return HttpResponse("Mi primer hello world en Django")


def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :) ")
    

def diaDeHoy(request):

        dia = datetime.now()

        documentoDeTexto = f"Hoy es día: <br> {dia}"


        return HttpResponse(documentoDeTexto)


def miNombreEs(self, nombre, edad):

    edad = int(edad)

    documentoDeTexto = f"Mi nombre es: <br><br>  {nombre} <br><br> Mi edad por 2 es: {edad * 2}"

    return HttpResponse(documentoDeTexto)


def calculate_birth_year(self, age):
    current_year = datetime.now().year
    birth_year = current_year - int(age)
    return HttpResponse(f"<br><br> My birth year is: {birth_year}")


def probandoTemplate(self):

    miHtml = open("D:/Miqueas/Git/Proyectos_Coder/class_17_Django/mysite/mysite/templates/template1.html")

    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context

    miHtml.close() #Cerramos el archivo

    miContexto = Context() #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo

    render = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento

    return HttpResponse(render)