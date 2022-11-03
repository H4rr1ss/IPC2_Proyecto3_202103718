from textwrap import indent
from django.shortcuts import render, HttpResponse
from .services.main_services import main_services
from .functions import handle_uploaded_file, xmlConfig, readConsumo
from .forms import UploadFileForm
from .clases import Recurso, RecursoConfig, Configuracion, Categoria, Instancia, Cliente, Consumo
from xml.etree import ElementTree as ET
import json
# Create your views here.


def main(request):
    Recursos = []
    Config = []
    instancias = []
    consulta = ''
    consulta = main_services.consultar()
    if request.method == 'POST':
        # Se recogen los datos de los forms para crear nuevos datos
        # -------------------Recursos-------------------------
        idRecurso = request.POST.get('id_recurso')
        nameRecurso = request.POST.get('name_recurso')
        abreviatura = request.POST.get('abr_recurso')
        metrica = request.POST.get('mtr_recurso')
        tipo = request.POST.get('tipo_recurso')
        precio = request.POST.get('precio_recurso')
        objrecurso = Recurso(idRecurso, nameRecurso,
                             abreviatura, metrica, tipo, precio)
        objRecursoJson = json.dumps(objrecurso.__dict__)
        main_services.Recursos({'objRecursos': objRecursoJson})
        # --------------------Configuración-------------------------------
        idConfig = request.POST.get('id_config')
        idCategoriaConfig = request.POST.get('id_config_categoria')
        nameConfig = request.POST.get('name_config')
        descConfig = request.POST.get('desc_config')
        idConfigRecurso = request.POST.get('id_config_recurso')
        cantidadRecurso = request.POST.get('cantidad_recurso')
        objRecursoConfig = RecursoConfig(idConfigRecurso, cantidadRecurso)
        Recursos.append(objRecursoConfig.__dict__)
        objConfig = Configuracion(
            idConfig, nameConfig, descConfig, Recursos)
        objConfig.idCategoria = idCategoriaConfig
        objConfigJson = json.dumps(objConfig.__dict__, indent=4)
        main_services.configuracion({'objConfig': objConfigJson})
        # -------------------Categoria----------------------------------
        idCategoria = request.POST.get('id_categoria')
        nameCategoria = request.POST.get('name_categoria')
        descCategoria = request.POST.get('desc_categoria')
        descCarga = request.POST.get('desc_carga')
        Config.append(objConfig.__dict__)
        objCategoria = Categoria(
            idCategoria, nameCategoria, descCategoria, descCarga, Config)
        objCategoriaJson = json.dumps(objCategoria.__dict__)
        main_services.categorias({'objCategoria': objCategoriaJson})
        # --------------------------Instancias-----------------------------
        idInstancia = request.POST.get('id_instancia')
        nitCliente = request.POST.get('nit_instancia')
        idConfigInstancia = request.POST.get('id_configu')
        nombreInstancia = request.POST.get('nombre_instancia')
        estado = request.POST.get('estado_instancia')
        fechaInicial = request.POST.get('inicio_instancia')
        fechaFinal = request.POST.get('final_instancia')
        objInstancia = Instancia(
            idInstancia, idConfigInstancia, nombreInstancia, fechaInicial, estado, fechaFinal)
        objInstancia.nitCliente = nitCliente
        objInstanciaJson = json.dumps(objInstancia.__dict__, indent=4)
        main_services.instancia({'objInstancia': objInstanciaJson})
        # -------------------------Clientes--------------------------------
        nit = request.POST.get('nit_cliente')
        nameCliente = request.POST.get('name_cliente')
        user = request.POST.get('user_cliente')
        clave = request.POST.get('clave_cliente')
        direccion = request.POST.get('address_cliente')
        mail = request.POST.get('mail_cliente')
        instancias.append(objInstancia.__dict__)
        objCliente = Cliente(nit, nameCliente, user, clave,
                             direccion, mail, instancias)
        objClienteJson = json.dumps(objCliente.__dict__)
        main_services.cliente({'objCliente': objClienteJson})
    return render(request, 'principal.html', {'json': consulta})


def xmlReader(request):
    result = ''
    lotRecurso = ''
    lotCategoria = ''
    lotCliente = ''
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            tree = ET.parse('main/upload/'+request.FILES['file'].name)
            rutaXML1 = tree.getroot()
            listRecursosJson, listCategoriaJSON, listClienteJson, lotRecurso, lotCategoria, lotCliente = xmlConfig(
                rutaXML1)
            result = main_services.rutaConfig(
                {'listRecursosJson': listRecursosJson, 'listCategoriasJSON': listCategoriaJSON, 'listaClientes': listClienteJson})
    else:
        form = UploadFileForm()

    return render(request, 'lector.html', {'form': form, 'result': result, 'recurso': lotRecurso, 'categoria': lotCategoria, 'cliente': lotCliente})


def xmlConsumo(request):
    consumo = ''
    lotConsumo = ''
    if request.method == 'POST':
        forms = UploadFileForm(request.POST, request.FILES)
        if forms.is_valid():
            handle_uploaded_file(request.FILES['file'])
            tree = ET.parse('main/upload/'+request.FILES['file'].name)
            rutaXML2 = tree.getroot()
            listconsumo, lotConsumo = readConsumo(rutaXML2)
            consumo = main_services.rutaConsumo(
                {'listConsumo': listconsumo, 'consumo': lotConsumo})
    else:
        forms = UploadFileForm()
    return render(request, 'consumo.html', {'forms': forms, 'consumo': lotConsumo})


def cancelar(request):
    cancel = ""
    if request.method == 'POST':
        nitCliente = request.POST.get('nit_cliente')
        idInstancia = request.POST.get('id_instancia')
        print(nitCliente, idInstancia)
        cancel = main_services.cancelar(
            {'nitCliente': nitCliente, 'idInstancia': idInstancia})
    return render(request, 'cancelar.html', {'msg': cancel})
