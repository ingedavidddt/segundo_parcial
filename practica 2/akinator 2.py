# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 18:13:39 2023

@author: david
"""
import json

class Arbol:
    def __init__(self, carga=None, izq=None, der=None):
        self.carga = carga
        self.izquierda = izq
        self.derecha = der

    def to_dict(self):
        if self.carga is None:
            return None
        return {
            'carga': self.carga,
            'izquierda': self.izquierda.to_dict() if self.izquierda else None,
            'derecha': self.derecha.to_dict() if self.derecha else None
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=2)

    @classmethod
    def from_dict(cls, data):
        if data is None:
            return None
        carga = data['carga']
        izquierda = cls.from_dict(data['izquierda']) if data['izquierda'] else None
        derecha = cls.from_dict(data['derecha']) if data['derecha'] else None
        return cls(carga, izquierda, derecha)

# -----------------------------------------------------------

# Funciones
# -----------------------------------------------------------

def si(preg):
    resp = input(preg).lower()
    return resp[0] == 's'

def cargar_arbol_desde_archivo(nombre_archivo='arbol.json'):
    try:
        with open(nombre_archivo, 'r') as archivo:
            data = json.load(archivo)
            return Arbol.from_dict(data)
    except FileNotFoundError:
        return None

def almacenar_arbol_en_archivo(arbol, nombre_archivo='arbol.json'):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(arbol.to_dict(), archivo, indent=2)

# -----------------------------------------------------------

def main():
    raiz = cargar_arbol_desde_archivo()
    if raiz is None:
        raiz = Arbol("pajaro")

    bucle = True
    while bucle:
        if not si("¿Estás pensando en un animal? "):
            almacenar_arbol_en_archivo(raiz)
            break

        arbol = raiz
        while arbol.izquierda is not None:
            if si(arbol.carga + "? "):
                arbol = arbol.izquierda
            else:
                arbol = arbol.derecha

        # Adivinar
        animal = arbol.carga
        if si("¿Es un " + animal + "? "):
            print("¡Soy el más grande!")
            continue

        # Obtener información
        nuevo = input("¿Qué animal era? ")
        info = input("¿Qué diferencia a un " + animal + " de un " + nuevo + "? ")
        indicador = "Si el animal fuera un " + animal + ", ¿cuál sería la respuesta? "
        arbol.carga = info
        if si(indicador):
            arbol.izquierda = Arbol(animal)
            arbol.derecha = Arbol(nuevo)
        else:
            arbol.derecha = Arbol(animal)
            arbol.izquierda = Arbol(nuevo)

    return 0

if __name__ == '__main__':
    main()
