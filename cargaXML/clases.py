class Recurso(object):
    def __init__(self, id, name, abbreviation, metrics, type, price):
        self.id = id
        self.name = name
        self.abbreviation = abbreviation
        self.metrics = metrics
        self.type = type
        self.price = price

# -------------------------------------------------------------------------------------------------------------------------

class RecursoConfig(object):
    def __init__(self, id, lot):
        self.id = id
        self.lot = lot
    

class Configuracion(object):
    def __init__(self, id, name, description, listRecursos):
        self.id = id
        self.name = name
        self.description = description
        self.listRecursos = listRecursos


class Categoria(object):
    def __init__(self, id, name, description, workload, listConfiguration):
        self.id = id
        self.name = name
        self.description = description
        self.workload = workload
        self.listConfiguration = listConfiguration

# -------------------------------------------------------------------------------------------------------------------------

class Instancia(object):
    def __init__(self, id, idConfig, name, dateInitial, status, dateFinal):
        self.id = id
        self.idConfig = idConfig
        self.name = name
        self.dateInitial = dateInitial
        self.status = status
        self.dateFinal = dateFinal

class Cliente(object):
    def __init__(self, nit, name, user, pasw, address, email, listInstance):
        self.nit = nit
        self.name = name
        self.user = user
        self.pasw = pasw
        self.address = address
        self.email = email
        self.listInstance = listInstance

# -------------------------------------------------------------------------------------------------------------------------
class Consumo(object):
    def __init__(self, nitCliente, idInstancia, tiempo, fechaHora):
        self.nitCliente = nitCliente
        self.idInstancia = idInstancia
        self.tiempo = tiempo
        self.fechaHora = fechaHora