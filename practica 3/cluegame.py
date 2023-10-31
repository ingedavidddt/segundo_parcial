# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 17:10:26 2023

@author: david
"""

import random

personajes = ["saber", "Rider", "lanzer", "archer", "assassin"]
armas = ["Candelabro", "Llave inglesa", "Cuerda", "Cuchillo", "Revólver"]
habitaciones = ["Casa", "patio", "Cuarto", "Cocina", "Sala"]
recubrimiento = ["mermelada", "capsu"]

# El sobre confidencial contiene las cartas del culpable

'''
sobre = {
    "personaje": random.choice(personajes),
    "arma": random.choice(armas),
    "habitacion": random.choice(habitaciones)
}
'''
def crear_sobre():
    sobre = {}
    
    sobre["culpable"] = random.choice(personajes)
    sobre["arma"] = random.choice(armas)
    sobre["lugar"] = random.choice(habitaciones)
    
    return sobre
    

def crear_historia (culpable, arma, lugar): 
    

    
    
    global pista1 
    pista1 = random.choice(personajes)
    
    while(pista1 == culpable):
        pista1 = random.choice(personajes)
    
    historia = f"se descubrio el cadaver de Caster en {lugar} ademas {pista1} vio un objeto manchado de sangre"
    print(historia)
    
    
    return pista1

def ubicar_objetos(culpable, arma, habitacion):
    
    Ht = habitaciones.copy()
    Pt = personajes.copy()
    At = armas.copy()
    
    #print("\n\n"+ habitacion+"\n\n")
   # Ht.remove(habitacion)
   # Pt.remove(culpable)
    #At.remove(arma)
    
    random.shuffle(habitaciones)
    random.shuffle(armas)
    random.shuffle(personajes)
    
    
    a_p = dict(zip(personajes, habitaciones))
    a_a = dict(zip(armas, habitaciones))
    
   # print(a_p)
   # print(a_a)
    return a_p, a_a
        
def jugar():
    
    sobre_confidencial =  crear_sobre()
    print(sobre_confidencial)
    
    sospechoso, ubicacionArma = ubicar_objetos(sobre_confidencial["culpable"], sobre_confidencial["arma"], sobre_confidencial["lugar"])
        
    #crear_historia(sobre_confidencial["culpable"], sobre_confidencial["arma"],sobre_confidencial["lugar"])
    
    Ucadaver = sobre_confidencial["lugar"]
     
    pista1 = random.choice(personajes)
    
    armaUsadaPista1 = sobre_confidencial["arma"]
    
    ubicacionArmaPista1 = ubicacionArma[armaUsadaPista1]
    
    historia = f"se descubrio el cadaver de Caster en {Ucadaver} ademas {pista1} vio lo que parece ser {armaUsadaPista1} cubierta de sangre en {ubicacionArmaPista1} "
    print(historia)
    
    intentos = 0
    x = ""
    posicionLista = 0
    while(intentos <= 5):
   
        print(f"tienes {5-intentos} aportunidades para encontrar al culpable a continucaion selecciona que es lo que quieres ver o hacer\npersonaje --> 1\narma--------> 2\nlugar ------> 3\nseleccionar culpable ----->4")
    
          
        x = input()
        
        
         #---------------------------------------personajes
        if(x == "1"):
            listaPersonajes = []
            
            print("a continuacion seleccione el personaje del que desea conocer su ubicacion")
            i=1
            
            for personaje in personajes:
                print(personaje + "---> ", i , "\n")
                listaPersonajes.append(personaje)
                i+=1
            
            personajeElegido = input()
            
            continuar = False
            
            while(continuar == False):
                if(personajeElegido == "1"):
                    posicionLista = 0
                    continuar = True
                elif(personajeElegido == "2"):
                    posicionLista = 1
                    continuar = True
                elif(personajeElegido == "3"):
                    posicionLista = 2
                    continuar = True
                elif(personajeElegido == "4"):
                    posicionLista = 3
                    continuar = True
                elif(personajeElegido == "5"):
                    posicionLista = 4
                    continuar = True
                else:
                    print("\n\nopcion invalida intente nuevamente\n\n")
            print(listaPersonajes)        
            ubicacionSospechoso = sospechoso[listaPersonajes[posicionLista]]
            print(f"{listaPersonajes[posicionLista]} dice que se encontraba en {ubicacionSospechoso}\n\n")
            
            intentos+=1
            
        #-------------------------------arma
        
        if(x == "2"):
            listaArmas = []
            posicionLista = 0
            print("a continuacion seleccione el arma del que desea conocer su ubicacion")
            i=1
            
            for arma in armas:
                print(arma + "---> ", i , "\n")
                listaArmas.append(arma)
                i+=1
            
            armaElegida = input()
            
            continuar = False
            
            while(continuar == False):
                if(armaElegida == "1"):
                    posicionLista = 0
                    continuar = True
                elif(armaElegida == "2"):
                    posicionLista = 1
                    continuar = True
                elif(armaElegida == "3"):
                    posicionLista = 2
                    continuar = True
                elif(armaElegida == "4"):
                    posicionLista = 3
                    continuar = True
                elif(armaElegida == "5"):
                    posicionLista = 4
                    continuar = True
                else:
                    print("\n\nopcion invalida intente nuevamente\n\n")
                    
            localizacionArma = ubicacionArma[listaArmas[posicionLista]]
            
            quienLaVio = ""
            
            for clave, valor in sospechoso.items():
                if valor == localizacionArma:
                    quienLaVio = clave
            
            print(f"{listaArmas[posicionLista]} fue encontraba en {localizacionArma} por {quienLaVio}\n\n")
            intentos+=1
        
        #------------------------------------lugar
            
        if(x == "3"):
            listaLugares = []
            posicionLista = 0
            print("a continuacion seleccione el arma del que desea conocer su ubicacion")
            i=1
            
            for lugar in habitaciones:
                print(lugar + "---> ", i , "\n")
                listaLugares.append(lugar)
                i+=1
            
            lugarElegido = input()
            
            continuar = False
            
            while(continuar == False):
                if(lugarElegido == "1"):
                    posicionLista = 0
                    continuar = True
                elif(lugarElegido == "2"):
                    posicionLista = 1
                    continuar = True
                elif(lugarElegido == "3"):
                    posicionLista = 2
                    continuar = True
                elif(lugarElegido == "4"):
                    posicionLista = 3
                    continuar = True
                elif(lugarElegido == "5"):
                    posicionLista = 4
                    continuar = True
                else:
                    print("\n\nopcion invalida intente nuevamente\n\n")
                    
            lugarEscogido = listaLugares[posicionLista]
            
            quienEstabaAhi = ""
            queArmaEstabaAhi = ""
            #persona el localizacion
            for clave, valor in sospechoso.items():
                if valor == lugarEscogido:
                    quienEstabaAhi = clave
             #arma en localizacion       
            for clave, valor in ubicacionArma.items():
                if valor == lugarEscogido:
                    queArmaEstabaAhi = clave                
                    
                  
            
            print(f" en {lugarEscogido} fue encontrado {queArmaEstabaAhi} mientras  {quienEstabaAhi} estaba en ese lugar \n\n")      
            
            intentos+=1
        
        
            
        if(x == "4" or intentos == 5):
            listaPersonajes = []
            posicionLista = 0
            print("a continuacion seleccione al personaje que crees que es el asesino")
            i=1
            
            for personaje in personajes:
                print(personaje + "---> ", i , "\n")
                listaPersonajes.append(personaje)
                i+=1
            
            personajeElegido = input()
            
            continuar = False
            
            while(continuar == False):
                if(personajeElegido == "1"):
                    posicionLista = 0
                    continuar = True
                elif(personajeElegido == "2"):
                    posicionLista = 1
                    continuar = True
                elif(personajeElegido == "3"):
                    posicionLista = 2
                    continuar = True
                elif(personajeElegido == "4"):
                    posicionLista = 3
                    continuar = True
                elif(personajeElegido == "5"):
                    posicionLista = 4
                    continuar = True
                else:
                    print("\n\nopcion invalida intente nuevamente\n\n")
                    
                    
                    
            supuestoAsesino = listaPersonajes[posicionLista]
            culpable = sobre_confidencial["culpable"]
            if(supuestoAsesino == culpable):
                print("eres ungenio resolviste el caso")
                break
            #elif(intentos<5):
                
                #print("has fallado te quedan ",4-intentos," intentos")
            else:
                print("has fallado el asesino fue mas listo que tu")
            intentos+=1  
                
                
    return None



continuar = "1"
while continuar != "2":
    continuar = input("bienvenido a clue que es lo que quieres hacer\njugar --> 1\nsalir --> 2\n")
    
    if(continuar == "1"):
        jugar()
    elif(continuar == "2"):
        print("gracias por jugar")
    else :
        print("opcion invalida intente nuevamente")


  
   
   