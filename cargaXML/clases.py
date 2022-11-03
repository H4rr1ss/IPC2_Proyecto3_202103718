class Recurso(object):
    def __init__(self, id, nombre, abreviatura, metrica, tipo, valorXhora):
        self.id = id
        self.nombre = nombre
        self.abreviatura = abreviatura
        self.metrica = metrica
        self.tipo = tipo
        self.valorXhora = valorXhora

# -------------------------------------------------------------------------------------------------------------------------


class RecursoConfig(object):
    def __init__(self, id, cantidad):
        self.id = id
        self.cantidad = cantidad


class Configuracion(object):
    def __init__(self, id, nombre, descripcion, listaRecursos):
        self.id = id
        self.idCategoria = ""
        self.nombre = nombre
        self.descripcion = descripcion
        self.listaRecursos = listaRecursos


class Categoria(object):
    def __init__(self, id, nombre, descripcion, cargaTrabajo, listaConfiguraciones):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.cargaTrabajo = cargaTrabajo
        self.listaConfiguraciones = listaConfiguraciones

# -------------------------------------------------------------------------------------------------------------------------


class Instancia(object):
    def __init__(self, id, idConfig, nombre, fechaInicio, estado, fechaFinal):
        self.id = id
        self.nitCliente = ""
        self.idConfig = idConfig
        self.nombre = nombre
        self.fechaInicio = fechaInicio
        self.estado = estado
        self.fechaFinal = fechaFinal


class Cliente(object):
    def __init__(self, nit, nombre, usuario, clave, direccion, correoElectronico, listaInstancias):
        self.nit = nit
        self.nombre = nombre
        self.usuario = usuario
        self.clave = clave
        self.direccion = direccion
        self.correoElectronico = correoElectronico
        self.listaInstancias = listaInstancias

# -----------------------------------------CLASE DE CONSUMO-------------------------------------------------------


class Consumo(object):
    def __init__(self, nitCliente, idInstancia, tiempo, fechaHora):
        self.nitCliente = nitCliente
        self.idInstancia = idInstancia
        self.tiempo = tiempo
        self.fechaHora = fechaHora