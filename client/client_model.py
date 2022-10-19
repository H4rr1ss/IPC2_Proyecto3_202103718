class Client_xml:
    def __init__(self, nit, name, user, key, address, email, listInstances):
        self.__nit = nit
        self.__name = name
        self.__user = user
        self.__key = key
        self.__address = address
        self.__email = email
        self.__listInstances = listInstances

    # GETTERS
    def getNit(self):
        return self.__nit

    def getName(self):
        return self.__name

    def getUser(self):
        return self.__user

    def getKey(self):
        return self.__key

    def getAddress(self):
        return self.__address

    def getEmail(self):
        return self.__email

    def getListInstances(self):
        return self.__listInstances


class Client_default:
    def __init__(self, name, nit, address):
        self.__name = name
        self.__nit = nit
        self.__address = address

    # GETTERS
    def getName(self):
        return self.__name

    def getNit(self):
        return self.__nit

    def getAddress(self):
        return self.__address
