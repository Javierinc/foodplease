from django.shortcuts import render

from productos.models import Producto

def mostrarIndex(request):
    return render(request, 'index.html')

def mostrarListado(request):
    prod = Producto.objects.all().values()
    datos = {'prod': prod}
    return render(request, 'listado.html', datos)


def mostrarFormularioRegistrar(request):
    return render(request, 'formulario_registrar.html')

def mostrarFormularioActualizar(request, id):
    try:
        prod = Producto.objects.get(id = id)
        datos = {'prod': prod}
        return render(request, 'formulario_actualizar.html', datos)
    except:
        prod = Producto.objects.all().values()
        datos = {'prod': prod, 'error': f"El id {id} no existe"}
        return render(request, 'listado.html', datos)

def insertarProducto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        prod = Producto(nombre=nombre, descripcion=descripcion, precio=precio)
        prod.save()
        datos = {'OK': 'Registro realizado correctamente 😁'}
        return render(request, 'formulario_registrar.html', datos)
    else:
        datos = {'error': 'Ouch! No se puede procesar su solicitud 😒'}
        return render(request, 'formulario_registrar.html', datos)

def actualizarProducto(request, id):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        prod = Producto.objects.get(id = id)
        prod.nombre = nombre
        prod.descripcion = descripcion
        prod.precio = precio
        prod.save()
        prod = Producto.objects.all().values()
        datos = {'prod': prod,'OK': 'Modificación de datos correcta 😁'}
        return render(request, 'listado.html', datos)
    else:
        datos = {'error': 'Ouch! No se puede procesar su solicitud 😒'}
        return render(request, 'listado.html', datos)
    
def eliminarProducto(request, id):
    try:
        prod = Producto.objects.get (id = id)
        prod.delete()
        prod = Producto.objects.all().values()
        datos = {'prod': prod, 'OK': "Registro eliminado exitosamente 😎"}
        return render(request, 'listado.html', datos)
    except:
        prod = Producto.objects.all().values()
        datos = {'prod': prod, 'error': f"El {id} no existe"}
        return render(request, 'listado.html', datos)