from django.http import HttpResponse

def MascotasPasto(request):

    return HttpResponse("MascotasPasto")

def salida(request):
    return HttpResponse("Hasta Luego de Mascotas Pasto")