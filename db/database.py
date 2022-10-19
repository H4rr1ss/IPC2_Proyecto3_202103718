import xml.etree.ElementTree as ET
import random
import string

class Database():
    def __init__(self):
        self.tree = ET.parse('./db/users.xml')
        self.root = self.tree.getroot()

# ------------------------------CREAR CLIENTE------------------------------
    def __userAndPassGenerator(self, name):
        numero = random.randint(0,300) + 1
        password = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))
        suf = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(2))
        user = '{}{}{}'.format(name, numero, suf)

        print('\nse realizo con exito total \ntu nick es: {} -> clave: {}'.format(user, password))
        return user, password

    def __writeUserXML(self, nit, name, address):
        new = ET.SubElement(self.root, 'cliente')

        ET.SubElement(new, 'nombre', nit='{}'.format(str(nit))).text='{}'.format(name)
        ET.SubElement(new, 'direccionF').text='{}'.format(address)

        user, password = self.__userAndPassGenerator(name)

        ET.SubElement(new, 'usuario').text='{}'.format(user)
        ET.SubElement(new, 'clave').text='{}'.format(password)

        self.tree.write('./db/users.xml', xml_declaration=True)
    
    def __searchClient(self, nit):
        for client in self.root:
            if client.tag == 'cliente':
                for data in client:
                    if data.tag == 'nombre':
                        nitXML = data.get('nit')
                        nameXML = data.text

                        if nitXML == nit:
                            print('el cliente: {} ya existe'.format(nameXML))
                            return True
        return False

    def createClient(self, name, nit, address):
        """(view: registrar)\n
        En esta funcion se verificará si existen clientes con el mismo nit ingresado dentro
        de la base de datos\n\n

        Posibles retornos:\n
        True: ~Encontró un nit identico al ingresado~\n
        False: ~No encontró ninguna coincidencia, se creará el cliente con éxito~
        """
        condition = self.__searchClient(nit)
        if condition is True:
            return True

        self.__writeUserXML(nit, name, address)
        return False
# --------------------------------------------------------------------------

# ----------------------VERIFICAR USUARIO Y CONTRASEÑA EXISTENTE----------------------
    def __searchUser(self, user, password):
        for client in self.root:
            if client.tag == 'cliente':
                contador = 0
                for data in client:
                    if data.tag == 'usuario':
                        userXML = data.text

                        if userXML == user:
                            contador += 1
                    
                    elif data.tag == 'clave':
                        passXML = data.text

                        if passXML == password:
                            contador += 1

                if str(contador) == '2':
                    return contador
        return None

    def userValidation(self, user, password):
        '''(view: login)\n
        En esta funcion se verificará si el username ya existe en el sistema y si la contraseña
        es la correcta para tener acceso a la manipulación de instancias\n\n

        Posibles retornos:\n
        True: ~No encontró al usuario en la base de datos o ~\n
        False: ~No encontró ninguna coincidencia, se creará el cliente con éxito~
        '''
        condition = self.__searchUser(user, password)

        if condition is not None:
            return True

        return False

# ------------------------------------------------------------------------------------

DB = Database()