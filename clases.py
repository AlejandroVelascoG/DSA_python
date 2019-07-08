#!/usr/bin/env python
# coding: utf-8

# In[ ]:




# ejercicio DSA

# Clase Tarjeta de crédito

class Tarjeta:

    # clase que representa una tarjeta de crédito con el nombre del cliente, el banco de la tarjeta
    # el número de la cuenta y el límite

    def __init__(self, cliente, banco, cuenta, limite):

        self._cliente = cliente
        self._banco = banco
        self._cuenta = cuenta
        self._limite = limite
        self._balance = 0

    def get_cliente(self):
        return self._cliente

    def get_banco(self):
        return self._banco

    def get_cuenta(self):
        return self._cuenta

    def get_limite(self):
        return self._limite

    def get_balance(self):
        return self._balance

    # Función para cargar a la tarjeta

    def cargar(self, precio):

        # Carga el precio dado a la tarjeta. Si la suma del precio y el balance exceden el límite,
        # no permite cargar a la tarjeta

        if precio + self._balance > self._limite:
            return False
        else:
            self._balance += precio
            return True

    # Función para pagar al banco

    def pagar(self, cantidad):
        # Reduce al balance la cantidad pagada
        self._balance -= cantidad

'''
En la definición de una clase, los métodos pueden aparecer con más parámetros de los que ve el usuario
al llamar al método. Por ejemplo, los get reciben por parámetro el identificador 'self', pero el usuario
no le pasa ningún parámetro al método. El int´erprete de python automáticamente liga la instancia con la que
se llama al método con el parámetro self (ej: tarj1.get_cuenta()).
'''
