import json


class persona(object):
    def __init__(self, name, age, dpi):
        self.name = name
        self.age = age
        self.dpi = dpi

    
obj = persona('harry', '18', '23423')

conversion = json.dumps(obj.__dict__)

print(obj)
print(conversion)


#DESERIALIZACION
new = persona(**json.loads(conversion))
print(new)

print('')

lista = ['pepe', '12', 'hola']
listaJson = json.dumps(lista)
print(listaJson)
print(lista)

newLista = json.loads(listaJson)

print(newLista[2])

