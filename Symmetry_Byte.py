#Symmetry Byte - by Brick Briceño - 2022

#Librerias uwu

import threading
import random
import time
from tkinter import *
from tkinter import messagebox
from pygame import mixer
from math import cos, sin, radians, pi

#Variables

#colores
color1 = "#591F1D"
color2 = "#225937"
color3 = "#272859"
color4 = "#59512A"

name_compas = "4/4"

ritmo_1 = [0, 0, 0, 0, 0, 0, 0, 0]
ritmo_2 = [0, 0, 0, 0, 0, 0, 0, 0]
ritmo_3 = [0, 0, 0, 0, 0, 0, 0, 0]
ritmo_4 = [0, 0, 0, 0, 0, 0, 0, 0]

"""
eu1a = 0
eu1b = 0
eu2a = 0
eu2b = 0
eu3a = 0
eu3b = 0
eu4a = 0
eu4b = 0
"""

Tempo = 128
figura = 2 #corchea

c_compas = 8
ms_tempo = 60/figura/Tempo

activador = False
claqueta_activada = False

#Ritmos
ritmo_1_c1 = [0, 0, 0, 0, 0, 0, 0, 0]
ritmo_2_c1 = [0, 0, 0, 0, 0, 0, 0, 0]
ritmo_3_c1 = [0, 0, 0, 0, 0, 0, 0, 0]
ritmo_4_c1 = [0, 0, 0, 0, 0, 0, 0, 0]

ritmo_1_c2 = [0, 0, 0, 0, 0, 0, 0, 0]
ritmo_2_c2 = [0, 0, 0, 0, 0, 0, 0, 0]
ritmo_3_c2 = [0, 0, 0, 0, 0, 0, 0, 0]
ritmo_4_c2 = [0, 0, 0, 0, 0, 0, 0, 0]

ritmo_1_c3 = [0, 0, 0, 0, 0, 0, 0, 0]
ritmo_2_c3 = [0, 0, 0, 0, 0, 0, 0, 0]
ritmo_3_c3 = [0, 0, 0, 0, 0, 0, 0, 0]
ritmo_4_c3 = [0, 0, 0, 0, 0, 0, 0, 0]

ritmo_1_c4 = [0, 0, 0, 0, 0, 0, 0, 0]
ritmo_2_c4 = [0, 0, 0, 0, 0, 0, 0, 0]
ritmo_3_c4 = [0, 0, 0, 0, 0, 0, 0, 0]
ritmo_4_c4 = [0, 0, 0, 0, 0, 0, 0, 0]



#esta esta lista revertida???
ritmo1_R = False
ritmo2_R = False
ritmo3_R = False
ritmo4_R = False

ritmo1_M = False
ritmo2_M = False
ritmo3_M = False
ritmo4_M = False

#Variables de Editor:

R1P1C1_activado = False
R2P1C1_activado = False
R3P1C1_activado = False
R4P1C1_activado = False
R1P2C1_activado = False
R2P2C1_activado = False
R3P2C1_activado = False
R4P2C1_activado = False
R1P3C1_activado = False
R2P3C1_activado = False
R3P3C1_activado = False
R4P3C1_activado = False
R1P4C1_activado = False
R2P4C1_activado = False
R3P4C1_activado = False
R4P4C1_activado = False
R1P5C1_activado = False
R2P5C1_activado = False
R3P5C1_activado = False
R4P5C1_activado = False
R1P6C1_activado = False
R2P6C1_activado = False
R3P6C1_activado = False
R4P6C1_activado = False
R1P7C1_activado = False
R2P7C1_activado = False
R3P7C1_activado = False
R4P7C1_activado = False
R1P8C1_activado = False
R2P8C1_activado = False
R3P8C1_activado = False
R4P8C1_activado = False
R1P1C2_activado = False
R2P1C2_activado = False
R3P1C2_activado = False
R4P1C2_activado = False
R1P2C2_activado = False
R2P2C2_activado = False
R3P2C2_activado = False
R4P2C2_activado = False
R1P3C2_activado = False
R2P3C2_activado = False
R3P3C2_activado = False
R4P3C2_activado = False
R1P4C2_activado = False
R2P4C2_activado = False
R3P4C2_activado = False
R4P4C2_activado = False
R1P5C2_activado = False
R2P5C2_activado = False
R3P5C2_activado = False
R4P5C2_activado = False
R1P6C2_activado = False
R2P6C2_activado = False
R3P6C2_activado = False
R4P6C2_activado = False
R1P7C2_activado = False
R2P7C2_activado = False
R3P7C2_activado = False
R4P7C2_activado = False
R1P8C2_activado = False
R2P8C2_activado = False
R3P8C2_activado = False
R4P8C2_activado = False
R1P1C3_activado = False
R2P1C3_activado = False
R3P1C3_activado = False
R4P1C3_activado = False
R1P2C3_activado = False
R2P2C3_activado = False
R3P2C3_activado = False
R4P2C3_activado = False
R1P3C3_activado = False
R2P3C3_activado = False
R3P3C3_activado = False
R4P3C3_activado = False
R1P4C3_activado = False
R2P4C3_activado = False
R3P4C3_activado = False
R4P4C3_activado = False
R1P5C3_activado = False
R2P5C3_activado = False
R3P5C3_activado = False
R4P5C3_activado = False
R1P6C3_activado = False
R2P6C3_activado = False
R3P6C3_activado = False
R4P6C3_activado = False
R1P7C3_activado = False
R2P7C3_activado = False
R3P7C3_activado = False
R4P7C3_activado = False
R1P8C3_activado = False
R2P8C3_activado = False
R3P8C3_activado = False
R4P8C3_activado = False
R1P1C4_activado = False
R2P1C4_activado = False
R3P1C4_activado = False
R4P1C4_activado = False
R1P2C4_activado = False
R2P2C4_activado = False
R3P2C4_activado = False
R4P2C4_activado = False
R1P3C4_activado = False
R2P3C4_activado = False
R3P3C4_activado = False
R4P3C4_activado = False
R1P4C4_activado = False
R2P4C4_activado = False
R3P4C4_activado = False
R4P4C4_activado = False
R1P5C4_activado = False
R2P5C4_activado = False
R3P5C4_activado = False
R4P5C4_activado = False
R1P6C4_activado = False
R2P6C4_activado = False
R3P6C4_activado = False
R4P6C4_activado = False
R1P7C4_activado = False
R2P7C4_activado = False
R3P7C4_activado = False
R4P7C4_activado = False
R1P8C4_activado = False
R2P8C4_activado = False
R3P8C4_activado = False
R4P8C4_activado = False


variables_boton_estado = [R1P1C1_activado, R1P2C1_activado, R1P3C1_activado, R1P4C1_activado, R1P5C1_activado, R1P6C1_activado,
R1P7C1_activado, R1P8C1_activado, R2P1C1_activado, R2P2C1_activado, R2P3C1_activado, R2P4C1_activado, R2P5C1_activado, R2P6C1_activado,
R2P7C1_activado, R2P8C1_activado, R3P1C1_activado, R3P2C1_activado, R3P3C1_activado, R3P4C1_activado, R3P5C1_activado, R3P6C1_activado,
R3P7C1_activado, R3P8C1_activado, R4P1C1_activado, R4P2C1_activado, R4P3C1_activado, R4P4C1_activado, R4P5C1_activado, R4P6C1_activado,
R4P7C1_activado, R4P8C1_activado, R1P1C2_activado, R1P2C2_activado, R1P3C2_activado, R1P4C2_activado, R1P5C2_activado, R1P6C2_activado,
R1P7C2_activado, R1P8C2_activado, R2P1C2_activado, R2P2C2_activado, R2P3C2_activado, R2P4C2_activado, R2P5C2_activado, R2P6C2_activado,
R2P7C2_activado, R2P8C2_activado, R3P1C2_activado, R3P2C2_activado, R3P3C2_activado, R3P4C2_activado, R3P5C2_activado, R3P6C2_activado,
R3P7C2_activado, R3P8C2_activado, R4P1C2_activado, R4P2C2_activado, R4P3C2_activado, R4P4C2_activado, R4P5C2_activado, R4P6C2_activado,
R4P7C2_activado, R4P8C2_activado, R1P1C3_activado, R1P2C3_activado, R1P3C3_activado, R1P4C3_activado, R1P5C3_activado, R1P6C3_activado,
R1P7C3_activado, R1P8C3_activado, R2P1C3_activado, R2P2C3_activado, R2P3C3_activado, R2P4C3_activado, R2P5C3_activado, R2P6C3_activado,
R2P7C3_activado, R2P8C3_activado, R3P1C3_activado, R3P2C3_activado, R3P3C3_activado, R3P4C3_activado, R3P5C3_activado, R3P6C3_activado,
R3P7C3_activado, R3P8C3_activado, R4P1C3_activado, R4P2C3_activado, R4P3C3_activado, R4P4C3_activado, R4P5C3_activado, R4P6C3_activado,
R4P7C3_activado, R4P8C3_activado, R1P1C4_activado, R1P2C4_activado, R1P3C4_activado, R1P4C4_activado, R1P5C4_activado, R1P6C4_activado,
R1P7C4_activado, R1P8C4_activado, R2P1C4_activado, R2P2C4_activado, R2P3C4_activado, R2P4C4_activado, R2P5C4_activado, R2P6C4_activado,
R2P7C4_activado, R2P8C4_activado, R3P1C4_activado, R3P2C4_activado, R3P3C4_activado, R3P4C4_activado, R3P5C4_activado, R3P6C4_activado,
R3P7C4_activado, R3P8C4_activado, R4P1C4_activado, R4P2C4_activado, R4P3C4_activado, R4P4C4_activado, R4P5C4_activado, R4P6C4_activado,
R4P7C4_activado, R4P8C4_activado]

#la siguiente variable de los botones del editor va al final para que que tkinter las defina primero XD


"""
los valores son estos
redonda = .25
blanca = .5
negra = 1
corchea = 2
semi corchea = 4
fusa = 8
semi fusa 16
"""


#Sonido:

buffer = 256

mixer.pre_init(44100,-16,1, buffer)
mixer.init()

ritmoAu1 = mixer.Sound("ritmo1.wav")
ritmoAu2 = mixer.Sound("ritmo2.wav")
ritmoAu3 = mixer.Sound("ritmo3.wav")
ritmoAu4 = mixer.Sound("ritmo4.wav")

claqueta_fuerte = mixer.Sound("golpe_fuerte.wav")
claqueta_suave = mixer.Sound("golpe_suave.wav")

#Sonidos de inicio y final:
inicio = mixer.Sound("inicio.wav")
final = mixer.Sound("final.wav")



#Funciones >:D

def print_Brick(mensaje):# se debe meter un solo argumento, no es como el print normal
    mensaje_1 = str(mensaje) + "\n"
    texto.insert("insert", mensaje_1)


"""

def print_Brick(str(mensaje)):# se debe meter un solo argumento, no es como el print normal
    mensaje_1 = str(mensaje) + "\n"
    texto.insert("insert", mensaje_1)

"""


def GeneradorBrick_v2(a, b, c):
    if a > b:
        print("A es mayor a B!!! ")#que si no no tendria sentido el calculo
        messagebox.showerror(message="El 1er Numero debe ser menor al 2do\n\nIntente otra vez :D", title="Error :(")
        #Pausar()
        return
    if a == 0:
        return [0 for i in range(c)]
  
    pattern = []    
    counts = []
    remainders = []
    divisor = b - a
    remainders.append(a)
    level = 0
    while True:
        counts.append(divisor // remainders[level])
        remainders.append(divisor % remainders[level])
        divisor = remainders[level]
        level = level + 1
        if remainders[level] <= 1:
            break
    counts.append(divisor)
    
    def build(level):
        if level == -1:
            pattern.append(0)
        elif level == -2:
            pattern.append(1)         
        else:
            for i in range(0, counts[level]):
                build(level - 1)
            if remainders[level] != 0:
                build(level - 2)
    
    build(level)
    i = pattern.index(1)
    pattern = pattern[i:] + pattern[0:i]

    n = 0
    final_pattern = []
    while c != len(final_pattern):
        if n == len(pattern):
            n = 0
        final_pattern.append(pattern[n])
        n += 1

    return final_pattern #Yeii :D

def lista_binaria_a_decimal(l1, l2, l3, l4, p):
    suma = 0
    if l1[p] == 1:
        suma += 1

    if l2[p] == 1:
        suma += 2

    if l3[p] == 1:
        suma += 4

    if l4[p] == 1:
        suma += 8 

    return suma

def convertir_valores_entrada(dato):
	a = ""
	b = ""

	numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	posicion = 0

	try:
		while dato[posicion] in numeros:
			a = a + dato[posicion]
			posicion += 1
	
		posicion += 1
	
		while dato[posicion] in numeros:
			b = b + dato[posicion]
			posicion += 1

	except:
		a = int(a)
		b = int(b)
		return a,b # los datos te los devuelve en forma de tupla :)
    

def reproductor():
    n_partitura = 1 #partitura numero tal
    a = 0 #posición del pulso
    while activador:
        canvas.create_line(257, 257, 257 + 16*sin(radians((a+1)*720)), 100 - 16*cos(radians((a+1)*720)), fill='red',width=9,arrow= LAST)
        #Cambiar de compas
        if n_partitura == 1:
            #print("Tempo:", Tempo)
            b = lista_binaria_a_decimal(ritmo_1_c1, ritmo_2_c1, ritmo_3_c1, ritmo_4_c1, a)

        elif n_partitura == 2:
            b = lista_binaria_a_decimal(ritmo_1_c2, ritmo_2_c2, ritmo_3_c2, ritmo_4_c2, a)

        elif n_partitura == 3:
            b = lista_binaria_a_decimal(ritmo_1_c3, ritmo_2_c3, ritmo_3_c3, ritmo_4_c3, a)

        elif n_partitura == 4:
            b = lista_binaria_a_decimal(ritmo_1_c4, ritmo_2_c4, ritmo_3_c4, ritmo_4_c4, a)

        #print_Brick(("Compas:", n_partitura, "posicion: ", str(a)))
        if a == 7:#Cantidad de corcheas 8 xd 
            n_partitura += 1
            a = 0
            if n_partitura == 5:
                n_partitura = 1
        else:
            a += 1

        #Claqueta
        if a == 1 and claqueta_activada:
            claqueta_fuerte.play()

        if a == 3 and claqueta_activada:
            claqueta_suave.play()

        if a == 5 and claqueta_activada:
            claqueta_suave.play()

        if a == 7 and claqueta_activada:
            claqueta_suave.play()


        #Reproducir

        if b == 1:
            ritmoAu1.play()
        
        if b == 2:
            ritmoAu2.play()
        
        if b == 3:
            ritmoAu1.play()
            ritmoAu2.play()

        if b == 4:
            ritmoAu3.play()

        if b == 5:
            ritmoAu1.play()
            ritmoAu3.play()

        if b == 6:
            ritmoAu2.play()
            ritmoAu3.play()

        if b == 7:
            ritmoAu1.play()
            ritmoAu2.play()
            ritmoAu3.play()

        if b == 8:
            ritmoAu4.play()

        if b == 9:
            ritmoAu1.play()
            ritmoAu4.play()

        if b == 10:
            ritmoAu2.play()
            ritmoAu4.play()

        if b == 11:
            ritmoAu1.play()
            ritmoAu2.play()
            ritmoAu4.play()

        if b == 12:
            ritmoAu3.play()
            ritmoAu4.play()

        if b == 13: #agarramela que me crece
            ritmoAu1.play()
            ritmoAu3.play()
            ritmoAu4.play()

        if b == 14:
            ritmoAu2.play()
            ritmoAu3.play()
            ritmoAu4.play()

        if b == 15:
            ritmoAu1.play()
            ritmoAu2.play()
            ritmoAu3.play()
            ritmoAu4.play()

        time.sleep(60/2/Tempo)


def fuerza_bruta(lista):
    print("La lista " + str(lista) + " se genera con:\n")
    c = len(lista)
    intentos = 0
    solucion = 0
    invertida = "No"
    for x in range(2):
        lista_corrida = 0
        while lista_corrida != c:
            a = 0
            b = 0
            while not a == b == 32:
                if a == b:
                    b += 1
                    a = 1
                else:
                    a += 1
                intentos += 1
                if GeneradorBrick_v2(a, b, c) == lista:
                    solucion += 1
                    print("Solucion #" + str(solucion) + "\n")
                    print("A: " + str(a) + " B: " + str(b) + " C: " + str(c) + "\nLista corrida:\n"
                    + str(lista_corrida) + " bytes a la izquierda\n¿Invertida? "
                    + invertida + "\nIntentos: " + str(intentos))

            lista = mover_ritmo_izquierda(lista)
            lista_corrida += 1

        lista.reverse()
        invertida = "Si"


#Funciones de Botones

def Play():
    #print("play")
    global activador
    if not activador:
        activador = True
        reproducir = threading.Thread(target=reproductor)
        reproducir.start()

def Pausar():
    print("pause")
    global activador
    activador = False

def Eu1():
    eu1a = convertir_valores_entrada(inEu1T.get())[0]
    eu1b = convertir_valores_entrada(inEu1T.get())[1]

    inEu1D.set("Cargando")

    global ritmo_1
    ritmo_1 = GeneradorBrick_v2(eu1a, eu1b, c_compas)

    inEu1D.set(str(eu1a) + "," + str(eu1b))
    global ritmo1_M
    ritmo1_M = False
    mute1.config(bg="gray6", fg="snow")

    global ritmo1_R
    if ritmo1_R:
        ritmo_1.reverse()

def Eu2():
    eu2a = convertir_valores_entrada(inEu2T.get())[0]
    eu2b = convertir_valores_entrada(inEu2T.get())[1]

    inEu2D.set("Cargando")

    global ritmo_2
    ritmo_2 = GeneradorBrick_v2(eu2a, eu2b, c_compas)

    inEu2D.set(str(eu2a) + "," + str(eu2b))

    global ritmo2_M
    ritmo2_M = False
    mute2.config(bg="gray6", fg="snow")

    global ritmo2_R
    if ritmo2_R:
        ritmo_2.reverse()

def Eu3():
    eu3a = convertir_valores_entrada(inEu3T.get())[0]
    eu3b = convertir_valores_entrada(inEu3T.get())[1]

    inEu3D.set("Cargando")

    global ritmo_3
    ritmo_3 = GeneradorBrick_v2(eu3a, eu3b, c_compas)

    inEu3D.set(str(eu3a) + "," + str(eu3b))

    global ritmo3_M
    ritmo3_M = False
    mute3.config(bg="gray6", fg="snow")

    global ritmo3_R
    if ritmo3_R:
        ritmo_3.reverse()

def Eu4():
    eu4a = convertir_valores_entrada(inEu4T.get())[0]
    eu4b = convertir_valores_entrada(inEu4T.get())[1]

    inEu4D.set("Cargando")

    global ritmo_4
    ritmo_4 = GeneradorBrick_v2(eu4a, eu4b, c_compas)

    inEu4D.set(str(eu4a) + "," + str(eu4b))

    global ritmo4_M
    ritmo4_M = False
    mute4.config(bg="gray6", fg="snow")

    global ritmo4_R
    if ritmo4_R:
        ritmo_4.reverse()


def cambiar_todo():
    Eu1()
    Eu2()
    Eu3()
    Eu4()


asignando_tempo = False
primer_pulso = True
tomaM = []
contador = 0

def redondear_tempo():
    global Tempo
    Tempo = round(Tempo)
    TempoD.set(Tempo)


def fun_asignando_tempo():
    global asignando_tempo
    if not asignando_tempo:
        asignando_tempo = True
        fun = threading.Thread(target=contador_ms)
        fun.start()

def tempo_manual(event):
    global presiono
    fun_asignando_tempo()#Esta función verifica se el contador sigue funcionando
    manualTempo.config(bg="lightgoldenrod", fg="black")
    presiono = True

def contador_ms():
    global tomaM
    global asignando_tempo
    global presiono
    global Tempo
    primera_vez = True
    contador = 0
    antes = TempoD.get()
    while contador <= 1:#"se apaga a los 2 segundos"
        time.sleep(0.01)#estos 2 valores deben ser iguales, hay que
        contador += 0.01#consegir el equilibrio en presición y dendimiento
        if presiono:
            presiono = False
            tomaM.append(contador)
            Tempo = round(60/(sum(tomaM)/len(tomaM)))# el ultimo valor define la cantidad de decimales del tempo
            TempoD.set(Tempo)
            contador = 0
            if primera_vez:
                TempoD.set(antes)
                tomaM.pop(0)
                primera_vez = False
    #Tempo = round(Tempo)
    print(tomaM)
    TempoD.set(Tempo)
    tomaM = []
    manualTempo.config(bg="slateblue4", fg="black")
    asignando_tempo = False


def invertir_lista(lista):
    lista_final = []
    for x in range(len(lista)):
        lista_final.append(int(not lista[x]))
    return lista_final


def Guardar():
    eu1a = convertir_valores_entrada(inEu1T.get())[0]
    eu1b = convertir_valores_entrada(inEu1T.get())[1]
    eu2a = convertir_valores_entrada(inEu2T.get())[0]
    eu2b = convertir_valores_entrada(inEu2T.get())[1]
    eu3a = convertir_valores_entrada(inEu3T.get())[0]
    eu3b = convertir_valores_entrada(inEu3T.get())[1]
    eu4a = convertir_valores_entrada(inEu4T.get())[0]
    eu4b = convertir_valores_entrada(inEu4T.get())[1]
    f = open ("partituras.txt", "a")
    f.write(time.strftime("Fecha: ""%x""\nHora: ""%I%p:%M:%S") + "\nTempo: " + str(Tempo) + "bpm\nCompas " + name_compas + "\n")

    if ritmo1_R:
        f.write("Ritmo 1: " + str(eu1a) + "," + str(eu1b) + " (R)\n")
    else:
        f.write("Ritmo 1: " + str(eu1a) + "," + str(eu1b) + "\n")

    if ritmo1_M:
        f.write(str(ritmo_1) + " (Mute)\n")
    else:
        f.write(str(ritmo_1) + "\n")


    if ritmo2_R:
        f.write("Ritmo 2: " + str(eu2a) + "," + str(eu2b) + " (R)\n")
    else:
        f.write("Ritmo 2: " + str(eu2a) + "," + str(eu2b) + "\n")

    if ritmo2_M:
        f.write(str(ritmo_2) + " (Mute)\n")
    else:
        f.write(str(ritmo_2) + "\n")


    if ritmo3_R:
        f.write("Ritmo 3: " + str(eu3a) + "," + str(eu3b) + " (R)\n")
    else:
        f.write("Ritmo 3: " + str(eu3a) + "," + str(eu3b) + "\n")

    if ritmo3_M:
        f.write(str(ritmo_3) + " (Mute)\n")
    else:
        f.write(str(ritmo_3) + "\n")


    if ritmo4_R:
        f.write("Ritmo 4: " + str(eu4a) + "," + str(eu4b) + " (R)\n")
    else:
        f.write("Ritmo 4: " + str(eu4a) + "," + str(eu4b) + "\n")

    if ritmo4_M:
        f.write(str(ritmo_4) + " (Mute)\n")
    else:
        f.write(str(ritmo_4) + "\n")

    f.write("\n")
    f.close()

def mute1():
    global ritmo1_M
    global ritmo_1
    ritmo1_M = not(ritmo1_M)
    if ritmo1_M:
        mute1.config(bg="red4", fg="black")
        ritmo_1 = [0 for i in range(c_compas)]
    else:
        mute1.config(bg="gray6", fg="snow")
        Eu1()

def mute2():
    global ritmo2_M
    global ritmo_2
    ritmo2_M = not(ritmo2_M)
    if ritmo2_M:
        mute2.config(bg="red4", fg="black")
        ritmo_2 = [0 for i in range(c_compas)]
    else:
        mute2.config(bg="gray6", fg="snow")
        Eu2()

def mute3():
    global ritmo3_M
    global ritmo_3
    ritmo3_M = not(ritmo3_M)
    if ritmo3_M:
        mute3.config(bg="red4", fg="black")
        ritmo_3 = [0 for i in range(c_compas)]
    else:
        mute3.config(bg="gray6", fg="snow")
        Eu3()

def mute4():
    global ritmo4_M
    global ritmo_4
    ritmo4_M = not(ritmo4_M)
    if ritmo4_M:
        mute4.config(bg="red4", fg="black")
        ritmo_4 = [0 for i in range(c_compas)]
    else:
        mute4.config(bg="gray6", fg="snow")
        Eu4()

def Revertir1():
    global ritmo1_R
    global ritmo_1
    ritmo_1.reverse()
    ritmo1_R = not(ritmo1_R)
    if ritmo1_R:
        revertir1.config(bg="DarkGoldenrod4", fg="black")
    else:
        revertir1.config(bg="gray7", fg="snow")

def Revertir2():
    global ritmo2_R
    global ritmo_2
    ritmo_2.reverse()
    ritmo2_R = not(ritmo2_R)
    if ritmo2_R:
        revertir2.config(bg="DarkGoldenrod4", fg="black")
    else:
        revertir2.config(bg="gray7", fg="snow")

def Revertir3():
    global ritmo3_R
    global ritmo_3
    ritmo_3.reverse()
    ritmo3_R = not(ritmo3_R)
    if ritmo3_R:
        revertir3.config(bg="DarkGoldenrod4", fg="black")
    else:
        revertir3.config(bg="gray7", fg="snow")

def Revertir4():
    global ritmo4_R
    global ritmo_4
    ritmo_4.reverse()
    ritmo4_R = not(ritmo4_R)
    if ritmo4_R:
        revertir4.config(bg="DarkGoldenrod4", fg="black")
    else:
        revertir4.config(bg="gray7", fg="snow")

def ritmos_no_revertidos():
    global ritmo1_R
    global ritmo2_R
    global ritmo3_R
    global ritmo4_R
    revertir1.config(bg="gray7", fg="snow")
    revertir2.config(bg="gray7", fg="snow")
    revertir3.config(bg="gray7", fg="snow")
    revertir4.config(bg="gray7", fg="snow")
    if ritmo1_R:
        ritmo_1.reverse()
    if ritmo2_R:
        ritmo_2.reverse()
    if ritmo3_R:
        ritmo_3.reverse()
    if ritmo4_R:
        ritmo_4.reverse()

    ritmo1_R = False
    ritmo2_R = False
    ritmo3_R = False
    ritmo4_R = False

def ritmos_revertidos():
    global ritmo1_R
    global ritmo2_R
    global ritmo3_R
    global ritmo4_R
    revertir1.config(bg="DarkGoldenrod4", fg="black")
    revertir2.config(bg="DarkGoldenrod4", fg="black")
    revertir3.config(bg="DarkGoldenrod4", fg="black")
    revertir4.config(bg="DarkGoldenrod4", fg="black")
    if not ritmo1_R:
        ritmo_1.reverse()
    if not ritmo2_R:
        ritmo_2.reverse()
    if not ritmo3_R:
        ritmo_3.reverse()
    if not ritmo4_R:
        ritmo_4.reverse()

    ritmo1_R = True
    ritmo2_R = True
    ritmo3_R = True
    ritmo4_R = True

def Revertir():
    if ritmo1_R * ritmo2_R * ritmo3_R * ritmo4_R:
        ritmos_no_revertidos()
    else:
        ritmos_revertidos()


def mover_ritmo_izquierda(lista_a_mover):
    lista_a_mover.append(lista_a_mover[0])
    lista_a_mover.pop(0)
    return lista_a_mover

def mover_ritmo_derecha(lista_a_mover):
    for i in range(len(lista_a_mover) -1):
        lista_a_mover.append(lista_a_mover[0])
        lista_a_mover.pop(0)
    return lista_a_mover

def mover_1_derecha():
    global ritmo_1
    ritmo_1 = mover_ritmo_derecha(ritmo_1)

def mover_2_derecha():
    global ritmo_2
    ritmo_2 = mover_ritmo_derecha(ritmo_2)

def mover_3_derecha():
    global ritmo_3
    ritmo_3 = mover_ritmo_derecha(ritmo_3)

def mover_4_derecha():
    global ritmo_4
    ritmo_4 = mover_ritmo_derecha(ritmo_4)


def mover_1_izquierda():
    global ritmo_1
    ritmo_1 = mover_ritmo_izquierda(ritmo_1)

def mover_2_izquierda():
    global ritmo_2
    ritmo_2 = mover_ritmo_izquierda(ritmo_2)

def mover_3_izquierda():
    global ritmo_3
    ritmo_3 = mover_ritmo_izquierda(ritmo_3)

def mover_4_izquierda():
    global ritmo_4
    ritmo_4 = mover_ritmo_izquierda(ritmo_4)


def Aleatorio(comando):
    print("Aleatorio")
    if comando == 1:#algoritmo 1
        while True:
            eu1a = random.randint(1, 24)
            eu1b = convertir_valores_entrada(inEu1T.get())[1]
            print("A:", eu1a, "B", eu1b)
            if eu1a <= eu1b:
                break
        ritmo_1 = GeneradorBrick_v2(eu1a, eu1b, c_compas)
        inEu1D.set(str(eu1a) + "," + str(eu1b))
        print(ritmo_1)
        revertir1.config(bg="gray7", fg="snow")

    if comando == 2:#algoritmo 2
        while True:
            eu1a = convertir_valores_entrada(inEu1T.get())[0]
            eu1b = random.randint(1, 24)
            if eu1a <= eu1b:
                break
        ritmo_1 = GeneradorBrick_v2(eu1a, eu1b, c_compas)
        inEu1D.set(str(eu1a) + "," + str(eu1b))
        print(ritmo_1)
        revertir1.config(bg="gray7", fg="snow")

    if comando == 3:#algoritmo 3
        while True:
            eu1a = random.randint(1, 24)
            eu1b = random.randint(1, 24)
            if eu1a <= eu1b:
                break
        ritmo_1 = GeneradorBrick_v2(eu1a, eu1b, c_compas)
        inEu1D.set(str(eu1a) + "," + str(eu1b))
        print(ritmo_1)
        revertir1.config(bg="gray7", fg="snow")


    if comando == 4:#algoritmo 1
        while True:
            eu2a = random.randint(1, 24)
            eu2b = convertir_valores_entrada(inEu2T.get())[1]
            if eu2a <= eu2b:
                break
        ritmo_2 = GeneradorBrick_v2(eu2a, eu2b, c_compas)
        inEu2D.set(str(eu2a) + "," + str(eu2b))
        print(ritmo_2)
        revertir2.config(bg="gray7", fg="snow")

    if comando == 5:#algoritmo 2
        while True:
            eu2a = convertir_valores_entrada(inEu2T.get())[0]
            eu2b = random.randint(1, 24)
            if eu2a <= eu2b:
                break
        ritmo_2 = GeneradorBrick_v2(eu2a, eu2b, c_compas)
        inEu2D.set(str(eu2a) + "," + str(eu2b))
        print(ritmo_2)
        revertir2.config(bg="gray7", fg="snow")

    if comando == 6:#algoritmo 3
        while True:
            eu2a = random.randint(1, 24)
            eu2b = random.randint(1, 24)
            if eu2a <= eu2b:
                break
        ritmo_2 = GeneradorBrick_v2(eu2a, eu2b, c_compas)
        inEu2D.set(str(eu2a) + "," + str(eu2b))
        print(ritmo_2)
        revertir2.config(bg="gray7", fg="snow")


    if comando == 7:#algoritmo 1
        while True:
            eu3a = random.randint(1, 24)
            eu3b = convertir_valores_entrada(inEu3T.get())[1]
            if eu3a <= eu3b:
                break
        ritmo_3 = GeneradorBrick_v2(eu3a, eu3b, c_compas)
        inEu3D.set(str(eu3a) + "," + str(eu3b))
        print(ritmo_3)
        revertir3.config(bg="gray7", fg="snow")

    if comando == 8:#algoritmo 2
        while True:
            eu3a = convertir_valores_entrada(inEu3T.get())[0]
            eu3b = random.randint(1, 24)
            if eu3a <= eu3b:
                break
        ritmo_3 = GeneradorBrick_v2(eu3a, eu3b, c_compas)
        inEu3D.set(str(eu3a) + "," + str(eu3b))
        print(ritmo_3)
        revertir3.config(bg="gray7", fg="snow")

    if comando == 9:#algoritmo 3
        while True:
            eu3a = random.randint(1, 24)
            eu3b = random.randint(1, 24)
            if eu3a <= eu3b:
                break
        ritmo_3 = GeneradorBrick_v2(eu3a, eu3b, c_compas)
        inEu3D.set(str(eu3a) + "," + str(eu3b))
        print(ritmo_3)
        revertir3.config(bg="gray7", fg="snow")


    if comando == 10:#algoritmo 1
        while True:
            eu4a = random.randint(1, 24)
            eu4b = convertir_valores_entrada(inEu4T.get())[1]
            if eu4a <= eu4b:
                break
        ritmo_4 = GeneradorBrick_v2(eu4a, eu4b, c_compas)
        inEu4D.set(str(eu4a) + "," + str(eu4b))
        print(ritmo_4)
        revertir4.config(bg="gray7", fg="snow")

    if comando == 11:#algoritmo 2
        while True:
            eu4a = convertir_valores_entrada(inEu4T.get())[0]
            eu4b = random.randint(1, 24)
            if eu4a <= eu4b:
                break
        ritmo_4 = GeneradorBrick_v2(eu4a, eu4b, c_compas)
        inEu4D.set(str(eu4a) + "," + str(eu4b))
        print(ritmo_4)
        revertir4.config(bg="gray7", fg="snow")

    if comando == 12:#algoritmo 3
        while True:
            eu4a = random.randint(1, 24)
            eu4b = random.randint(1, 24)
            if eu4a <= eu4b:
                break
        ritmo_4 = GeneradorBrick_v2(eu4a, eu4b, c_compas)
        inEu4D.set(str(eu4a) + "," + str(eu4b))
        print(ritmo_4)
        revertir4.config(bg="gray7", fg="snow")


    if comando == 13: #tempo jaja
        global Tempo
        Tempo = random.randint(75, 160)
        TempoD.set(Tempo)
        print("Tempo:", Tempo)


def ramdon1_r1():
    Aleatorio(1)

def ramdon2_r1():
    Aleatorio(2)

def ramdon3_r1():
    Aleatorio(3)


def ramdon1_r2():
    Aleatorio(4)

def ramdon2_r2():
    Aleatorio(5)

def ramdon3_r2():
    Aleatorio(6)


def ramdon1_r3():
    Aleatorio(7)

def ramdon2_r3():
    Aleatorio(8)

def ramdon3_r3():
    Aleatorio(9)


def ramdon1_r4():
    Aleatorio(10)

def ramdon2_r4():
    Aleatorio(11)

def ramdon3_r4():
    Aleatorio(12)

def ramdon_tempo():
    Aleatorio(13)


def ramdon_todo():
    for i in range(1, 13):
        print("hola", i)
        Aleatorio(i)


def claqueta():
    #print("claqueta activada")
    global claqueta_activada
    if claqueta_activada == False:
        claqueta_activada = True
        claqueta.config(bg="snow", fg="gray10")
    else:
        #print("claqueta desactivada")
        claqueta_activada = False
        claqueta.config(bg="gray10", fg="snow")

#Enviar a:

def enviar_c1():
    print("enviado a partitura 1")
    global ritmo_1_c1
    global ritmo_2_c1
    global ritmo_3_c1
    global ritmo_4_c1

    ritmo_1_c1 = ritmo_1
    ritmo_2_c1 = ritmo_2
    ritmo_3_c1 = ritmo_3
    ritmo_4_c1 = ritmo_4

    acualizar_botones(1)


def enviar_c2():
    print("enviado a partitura 2")
    global ritmo_1_c2
    global ritmo_2_c2
    global ritmo_3_c2
    global ritmo_4_c2

    ritmo_1_c2 = ritmo_1
    ritmo_2_c2 = ritmo_2
    ritmo_3_c2 = ritmo_3
    ritmo_4_c2 = ritmo_4

    acualizar_botones(2)


def enviar_c3():
    print("enviado a partitura 3")
    global ritmo_1_c3
    global ritmo_2_c3
    global ritmo_3_c3
    global ritmo_4_c3

    ritmo_1_c3 = ritmo_1
    ritmo_2_c3 = ritmo_2
    ritmo_3_c3 = ritmo_3
    ritmo_4_c3 = ritmo_4
    
    acualizar_botones(3)


def enviar_c4():
    print("enviado a partitura 4")
    global ritmo_1_c4
    global ritmo_2_c4
    global ritmo_3_c4
    global ritmo_4_c4

    ritmo_1_c4 = ritmo_1
    ritmo_2_c4 = ritmo_2
    ritmo_3_c4 = ritmo_3
    ritmo_4_c4 = ritmo_4
    
    acualizar_botones(4)


#Funciones de Editor:


def acualizar_botones(compas):#actualizar encendido de botones de editor y su valor booleano segun las listas
    print_ritmos()
    global variables_boton_estado, ritmo_1_c1, ritmo_2_c1, ritmo_3_c1, ritmo_4_c1, ritmo_1_c2, ritmo_2_c2, ritmo_3_c2, ritmo_4_c2, ritmo_1_c3, ritmo_2_c3, ritmo_3_c3, ritmo_4_c3, ritmo_1_c4, ritmo_2_c4, ritmo_3_c4, ritmo_4_c4
    if compas == 1:
        y = 0
        
        for x in range(8):#R1__C1
            if ritmo_1_c1[x] == 0: #si la posición tiene silencio, osea 0
                variables_boton_estado[x+y] = False
                numero_boton[x+y].config(bg="gray7")
            else:
                variables_boton_estado[x] = True
                numero_boton[x+y].config(bg=color1)

        y += 8

        for x in range(8):#R2
            if ritmo_2_c1[x] == 0: #si la posición tiene silencio, osea 0
                variables_boton_estado[x+y] = False
                numero_boton[x+y].config(bg="gray7")
            else:
                variables_boton_estado[x] = True
                numero_boton[x+y].config(bg=color1)
        y += 8

        for x in range(8):#R3
            if ritmo_3_c1[x] == 0: #si la posición tiene silencio, osea 0
                variables_boton_estado[x+y] = False
                numero_boton[x+y].config(bg="gray7")
            else:
                variables_boton_estado[x] = True
                numero_boton[x+y].config(bg=color1)
        y += 8

        for x in range(8):#R4
            if ritmo_4_c1[x] == 0: #si la posición tiene silencio, osea 0
                variables_boton_estado[x+y] = False
                numero_boton[x+y].config(bg="gray7")
            else:
                variables_boton_estado[x] = True
                numero_boton[x+y].config(bg=color1)
        y += 8

    if compas == 2:
        y = 32
        for x in range(8):#R1__C2
            if ritmo_1_c2[x] == 0: #si la posición tiene silencio, osea 0
                variables_boton_estado[x+y] = False
                numero_boton[x+y].config(bg="gray7")
            else:
                variables_boton_estado[x] = True
                numero_boton[x+y].config(bg=color2)

        y += 8

        for x in range(8):#R2
            if ritmo_2_c2[x] == 0: #si la posición tiene silencio, osea 0
                variables_boton_estado[x+y] = False
                numero_boton[x+y].config(bg="gray7")
            else:
                variables_boton_estado[x] = True
                numero_boton[x+y].config(bg=color2)
        y += 8

        for x in range(8):#R3
            if ritmo_3_c2[x] == 0: #si la posición tiene silencio, osea 0
                variables_boton_estado[x+y] = False
                numero_boton[x+y].config(bg="gray7")
            else:
                variables_boton_estado[x] = True
                numero_boton[x+y].config(bg=color2)
        y += 8

        for x in range(8):#R4
            if ritmo_4_c2[x] == 0: #si la posición tiene silencio, osea 0
                variables_boton_estado[x+y] = False
                numero_boton[x+y].config(bg="gray7")
            else:
                variables_boton_estado[x] = True
                numero_boton[x+y].config(bg=color2)
        y += 8

    if compas == 3:
        y = 64
        for x in range(8):#R1__C3
            if ritmo_1_c3[x] == 0: #si la posición tiene silencio, osea 0
                variables_boton_estado[x+y] = False
                numero_boton[x+y].config(bg="gray7")
            else:
                variables_boton_estado[x] = True
                numero_boton[x+y].config(bg=color3)

        y += 8

        for x in range(8):#R2
            if ritmo_2_c3[x] == 0: #si la posición tiene silencio, osea 0
                variables_boton_estado[x+y] = False
                numero_boton[x+y].config(bg="gray7")
            else:
                variables_boton_estado[x] = True
                numero_boton[x+y].config(bg=color3)
        y += 8

        for x in range(8):#R3
            if ritmo_3_c3[x] == 0: #si la posición tiene silencio, osea 0
                variables_boton_estado[x+y] = False
                numero_boton[x+y].config(bg="gray7")
            else:
                variables_boton_estado[x] = True
                numero_boton[x+y].config(bg=color3)
        y += 8

        for x in range(8):#R4
            if ritmo_4_c3[x] == 0: #si la posición tiene silencio, osea 0
                variables_boton_estado[x+y] = False
                numero_boton[x+y].config(bg="gray7")
            else:
                variables_boton_estado[x] = True
                numero_boton[x+y].config(bg=color3)
        y += 8

    if compas == 4:
        y = 96
        for x in range(8):#R1__C4
            if ritmo_1_c4[x] == 0: #si la posición tiene silencio, osea 0
                variables_boton_estado[x+y] = False
                numero_boton[x+y].config(bg="gray7")
            else:
                variables_boton_estado[x] = True
                numero_boton[x+y].config(bg=color4)

        y += 8

        for x in range(8):#R2
            if ritmo_2_c4[x] == 0: #si la posición tiene silencio, osea 0
                variables_boton_estado[x+y] = False
                numero_boton[x+y].config(bg="gray7")
            else:
                variables_boton_estado[x] = True
                numero_boton[x+y].config(bg=color4)
        y += 8

        for x in range(8):#R3
            if ritmo_3_c4[x] == 0: #si la posición tiene silencio, osea 0
                variables_boton_estado[x+y] = False
                numero_boton[x+y].config(bg="gray7")
            else:
                variables_boton_estado[x] = True
                numero_boton[x+y].config(bg=color4)
        y += 8

        for x in range(8):#R4
            if ritmo_4_c4[x] == 0: #si la posición tiene silencio, osea 0
                variables_boton_estado[x+y] = False
                numero_boton[x+y].config(bg="gray7")
            else:
                variables_boton_estado[x] = True
                numero_boton[x+y].config(bg=color4)
        y += 8

def print_ritmos():
    print("ritmo_1_c1", ritmo_1_c1)
    print("ritmo_2_c1", ritmo_2_c1)
    print("ritmo_3_c1", ritmo_3_c1)
    print("ritmo_4_c1", ritmo_4_c1)
    print("ritmo_1_c2", ritmo_1_c2)
    print("ritmo_2_c2", ritmo_2_c2)
    print("ritmo_3_c2", ritmo_3_c2)
    print("ritmo_4_c2", ritmo_4_c2)
    print("ritmo_1_c3", ritmo_1_c3)
    print("ritmo_2_c3", ritmo_2_c3)
    print("ritmo_3_c3", ritmo_3_c3)
    print("ritmo_4_c3", ritmo_4_c3)
    print("ritmo_1_c4", ritmo_1_c4)
    print("ritmo_2_c4", ritmo_2_c4)
    print("ritmo_3_c4", ritmo_3_c4)
    print("ritmo_4_c4", ritmo_4_c4)


#Funciones botones de editor

def holaa():
    print(variables_boton_estado)
    print(ritmo_1_c1)

def boton_R1P1C1():
    global variables_boton_estado, ritmo_1_c1
    if variables_boton_estado[0]:
        variables_boton_estado[0] = False
        R1P1C1.config(bg="gray7")
        ritmo_1_c1[0] = 0
        print(variables_boton_estado)
        print(ritmo_1_c1)
        print()
        holaa()




    else:
        variables_boton_estado[0] = True
        numero_boton[0].config(bg=color1)
        ritmo_1_c1[0] = 1

def boton_R1P2C1():
    global variables_boton_estado, ritmo_1_c1
    if variables_boton_estado[1]:
        variables_boton_estado[1] = False
        R1P2C1.config(bg="gray7")
        ritmo_1_c1[1] = 0
    else:
        variables_boton_estado[1] = True
        numero_boton[1].config(bg=color1)
        ritmo_1_c1[1] = 1

def boton_R1P3C1():
    global variables_boton_estado, ritmo_1_c1
    if variables_boton_estado[2]:
        variables_boton_estado[2] = False
        R1P3C1.config(bg="gray7")
        ritmo_1_c1[2] = 0
    else:
        variables_boton_estado[2] = True
        numero_boton[2].config(bg=color1)
        ritmo_1_c1[2] = 1

def boton_R1P4C1():
    global variables_boton_estado, ritmo_1_c1
    if variables_boton_estado[3]:
        variables_boton_estado[3] = False
        R1P4C1.config(bg="gray7")
        ritmo_1_c1[3] = 0
    else:
        variables_boton_estado[3] = True
        numero_boton[3].config(bg=color1)
        ritmo_1_c1[3] = 1

def boton_R1P5C1():
    global variables_boton_estado, ritmo_1_c1
    if variables_boton_estado[4]:
        variables_boton_estado[4] = False
        R1P5C1.config(bg="gray7")
        ritmo_1_c1[4] = 0
    else:
        variables_boton_estado[4] = True
        numero_boton[4].config(bg=color1)
        ritmo_1_c1[4] = 1

def boton_R1P6C1():
    global variables_boton_estado, ritmo_1_c1
    if variables_boton_estado[5]:
        variables_boton_estado[5] = False
        R1P6C1.config(bg="gray7")
        ritmo_1_c1[5] = 0
    else:
        variables_boton_estado[5] = True
        numero_boton[5].config(bg=color1)
        ritmo_1_c1[5] = 1

def boton_R1P7C1():
    global variables_boton_estado, ritmo_1_c1
    if variables_boton_estado[6]:
        variables_boton_estado[6] = False
        R1P7C1.config(bg="gray7")
        ritmo_1_c1[6] = 0
    else:
        variables_boton_estado[6] = True
        numero_boton[6].config(bg=color1)
        ritmo_1_c1[6] = 1

def boton_R1P8C1():
    global variables_boton_estado, ritmo_1_c1
    if variables_boton_estado[7]:
        variables_boton_estado[7] = False
        R1P8C1.config(bg="gray7")
        ritmo_1_c1[7] = 0
    else:
        variables_boton_estado[7] = True
        numero_boton[7].config(bg=color1)
        ritmo_1_c1[7] = 1

def boton_R2P1C1():
    global variables_boton_estado, ritmo_2_c1
    if variables_boton_estado[8]:
        variables_boton_estado[8] = False
        R2P1C1.config(bg="gray7")
        ritmo_2_c1[0] = 0
    else:
        variables_boton_estado[8] = True
        numero_boton[8].config(bg=color1)
        ritmo_2_c1[0] = 1

def boton_R2P2C1():
    global variables_boton_estado, ritmo_2_c1
    if variables_boton_estado[9]:
        variables_boton_estado[9] = False
        R2P2C1.config(bg="gray7")
        ritmo_2_c1[1] = 0
    else:
        variables_boton_estado[9] = True
        numero_boton[9].config(bg=color1)
        ritmo_2_c1[1] = 1

def boton_R2P3C1():
    global variables_boton_estado, ritmo_2_c1
    if variables_boton_estado[10]:
        variables_boton_estado[10] = False
        R2P3C1.config(bg="gray7")
        ritmo_2_c1[2] = 0
    else:
        variables_boton_estado[10] = True
        numero_boton[10].config(bg=color1)
        ritmo_2_c1[2] = 1

def boton_R2P4C1():
    global variables_boton_estado, ritmo_2_c1
    if variables_boton_estado[11]:
        variables_boton_estado[11] = False
        R2P4C1.config(bg="gray7")
        ritmo_2_c1[3] = 0
    else:
        variables_boton_estado[11] = True
        numero_boton[11].config(bg=color1)
        ritmo_2_c1[3] = 1

def boton_R2P5C1():
    global variables_boton_estado, ritmo_2_c1
    if variables_boton_estado[12]:
        variables_boton_estado[12] = False
        R2P5C1.config(bg="gray7")
        ritmo_2_c1[4] = 0
    else:
        variables_boton_estado[12] = True
        numero_boton[12].config(bg=color1)
        ritmo_2_c1[4] = 1

def boton_R2P6C1():
    global variables_boton_estado, ritmo_2_c1
    if variables_boton_estado[13]:
        variables_boton_estado[13] = False
        R2P6C1.config(bg="gray7")
        ritmo_2_c1[5] = 0
    else:
        variables_boton_estado[13] = True
        numero_boton[13].config(bg=color1)
        ritmo_2_c1[5] = 1

def boton_R2P7C1():
    global variables_boton_estado, ritmo_2_c1
    if variables_boton_estado[14]:
        variables_boton_estado[14] = False
        R2P7C1.config(bg="gray7")
        ritmo_2_c1[6] = 0
    else:
        variables_boton_estado[14] = True
        numero_boton[14].config(bg=color1)
        ritmo_2_c1[6] = 1

def boton_R2P8C1():
    global variables_boton_estado, ritmo_2_c1
    if variables_boton_estado[15]:
        variables_boton_estado[15] = False
        R2P8C1.config(bg="gray7")
        ritmo_2_c1[7] = 0
    else:
        variables_boton_estado[15] = True
        numero_boton[15].config(bg=color1)
        ritmo_2_c1[7] = 1

def boton_R3P1C1():
    global variables_boton_estado, ritmo_3_c1
    if variables_boton_estado[16]:
        variables_boton_estado[16] = False
        R3P1C1.config(bg="gray7")
        ritmo_3_c1[0] = 0
    else:
        variables_boton_estado[16] = True
        numero_boton[16].config(bg=color1)
        ritmo_3_c1[0] = 1

def boton_R3P2C1():
    global variables_boton_estado, ritmo_3_c1
    if variables_boton_estado[17]:
        variables_boton_estado[17] = False
        R3P2C1.config(bg="gray7")
        ritmo_3_c1[1] = 0
    else:
        variables_boton_estado[17] = True
        numero_boton[17].config(bg=color1)
        ritmo_3_c1[1] = 1

def boton_R3P3C1():
    global variables_boton_estado, ritmo_3_c1
    if variables_boton_estado[18]:
        variables_boton_estado[18] = False
        R3P3C1.config(bg="gray7")
        ritmo_3_c1[2] = 0
    else:
        variables_boton_estado[18] = True
        numero_boton[18].config(bg=color1)
        ritmo_3_c1[2] = 1

def boton_R3P4C1():
    global variables_boton_estado, ritmo_3_c1
    if variables_boton_estado[19]:
        variables_boton_estado[19] = False
        R3P4C1.config(bg="gray7")
        ritmo_3_c1[3] = 0
    else:
        variables_boton_estado[19] = True
        numero_boton[19].config(bg=color1)
        ritmo_3_c1[3] = 1

def boton_R3P5C1():
    global variables_boton_estado, ritmo_3_c1
    if variables_boton_estado[20]:
        variables_boton_estado[20] = False
        R3P5C1.config(bg="gray7")
        ritmo_3_c1[4] = 0
    else:
        variables_boton_estado[20] = True
        numero_boton[20].config(bg=color1)
        ritmo_3_c1[4] = 1

def boton_R3P6C1():
    global variables_boton_estado, ritmo_3_c1
    if variables_boton_estado[21]:
        variables_boton_estado[21] = False
        R3P6C1.config(bg="gray7")
        ritmo_3_c1[5] = 0
    else:
        variables_boton_estado[21] = True
        numero_boton[21].config(bg=color1)
        ritmo_3_c1[5] = 1

def boton_R3P7C1():
    global variables_boton_estado, ritmo_3_c1
    if variables_boton_estado[22]:
        variables_boton_estado[22] = False
        R3P7C1.config(bg="gray7")
        ritmo_3_c1[6] = 0
    else:
        variables_boton_estado[22] = True
        numero_boton[22].config(bg=color1)
        ritmo_3_c1[6] = 1

def boton_R3P8C1():
    global variables_boton_estado, ritmo_3_c1
    if variables_boton_estado[23]:
        variables_boton_estado[23] = False
        R3P8C1.config(bg="gray7")
        ritmo_3_c1[7] = 0
    else:
        variables_boton_estado[23] = True
        numero_boton[23].config(bg=color1)
        ritmo_3_c1[7] = 1

def boton_R4P1C1():
    global variables_boton_estado, ritmo_4_c1
    if variables_boton_estado[24]:
        variables_boton_estado[24] = False
        R4P1C1.config(bg="gray7")
        ritmo_4_c1[0] = 0
    else:
        variables_boton_estado[24] = True
        numero_boton[24].config(bg=color1)
        ritmo_4_c1[0] = 1

def boton_R4P2C1():
    global variables_boton_estado, ritmo_4_c1
    if variables_boton_estado[25]:
        variables_boton_estado[25] = False
        R4P2C1.config(bg="gray7")
        ritmo_4_c1[1] = 0
    else:
        variables_boton_estado[25] = True
        numero_boton[25].config(bg=color1)
        ritmo_4_c1[1] = 1

def boton_R4P3C1():
    global variables_boton_estado, ritmo_4_c1
    if variables_boton_estado[26]:
        variables_boton_estado[26] = False
        R4P3C1.config(bg="gray7")
        ritmo_4_c1[2] = 0
    else:
        variables_boton_estado[26] = True
        numero_boton[26].config(bg=color1)
        ritmo_4_c1[2] = 1

def boton_R4P4C1():
    global variables_boton_estado, ritmo_4_c1
    if variables_boton_estado[27]:
        variables_boton_estado[27] = False
        R4P4C1.config(bg="gray7")
        ritmo_4_c1[3] = 0
    else:
        variables_boton_estado[27] = True
        numero_boton[27].config(bg=color1)
        ritmo_4_c1[3] = 1

def boton_R4P5C1():
    global variables_boton_estado, ritmo_4_c1
    if variables_boton_estado[28]:
        variables_boton_estado[28] = False
        R4P5C1.config(bg="gray7")
        ritmo_4_c1[4] = 0
    else:
        variables_boton_estado[28] = True
        numero_boton[28].config(bg=color1)
        ritmo_4_c1[4] = 1

def boton_R4P6C1():
    global variables_boton_estado, ritmo_4_c1
    if variables_boton_estado[29]:
        variables_boton_estado[29] = False
        R4P6C1.config(bg="gray7")
        ritmo_4_c1[5] = 0
    else:
        variables_boton_estado[29] = True
        numero_boton[29].config(bg=color1)
        ritmo_4_c1[5] = 1

def boton_R4P7C1():
    global variables_boton_estado, ritmo_4_c1
    if variables_boton_estado[30]:
        variables_boton_estado[30] = False
        R4P7C1.config(bg="gray7")
        ritmo_4_c1[6] = 0
    else:
        variables_boton_estado[30] = True
        numero_boton[30].config(bg=color1)
        ritmo_4_c1[6] = 1

def boton_R4P8C1():
    global variables_boton_estado, ritmo_4_c1
    if variables_boton_estado[31]:
        variables_boton_estado[31] = False
        R4P8C1.config(bg="gray7")
        ritmo_4_c1[7] = 0
    else:
        variables_boton_estado[31] = True
        numero_boton[31].config(bg=color1)
        ritmo_4_c1[7] = 1

def boton_R1P1C2():
    global variables_boton_estado, ritmo_1_c2
    if variables_boton_estado[32]:
        variables_boton_estado[32] = False
        R1P1C2.config(bg="gray7")
        ritmo_1_c2[0] = 0
    else:
        variables_boton_estado[32] = True
        numero_boton[32].config(bg=color2)
        ritmo_1_c2[0] = 1

def boton_R1P2C2():
    global variables_boton_estado, ritmo_1_c2
    if variables_boton_estado[33]:
        variables_boton_estado[33] = False
        R1P2C2.config(bg="gray7")
        ritmo_1_c2[1] = 0
    else:
        variables_boton_estado[33] = True
        numero_boton[33].config(bg=color2)
        ritmo_1_c2[1] = 1

def boton_R1P3C2():
    global variables_boton_estado, ritmo_1_c2
    if variables_boton_estado[34]:
        variables_boton_estado[34] = False
        R1P3C2.config(bg="gray7")
        ritmo_1_c2[2] = 0
    else:
        variables_boton_estado[34] = True
        numero_boton[34].config(bg=color2)
        ritmo_1_c2[2] = 1

def boton_R1P4C2():
    global variables_boton_estado, ritmo_1_c2
    if variables_boton_estado[35]:
        variables_boton_estado[35] = False
        R1P4C2.config(bg="gray7")
        ritmo_1_c2[3] = 0
    else:
        variables_boton_estado[35] = True
        numero_boton[35].config(bg=color2)
        ritmo_1_c2[3] = 1

def boton_R1P5C2():
    global variables_boton_estado, ritmo_1_c2
    if variables_boton_estado[36]:
        variables_boton_estado[36] = False
        R1P5C2.config(bg="gray7")
        ritmo_1_c2[4] = 0
    else:
        variables_boton_estado[36] = True
        numero_boton[36].config(bg=color2)
        ritmo_1_c2[4] = 1

def boton_R1P6C2():
    global variables_boton_estado, ritmo_1_c2
    if variables_boton_estado[37]:
        variables_boton_estado[37] = False
        R1P6C2.config(bg="gray7")
        ritmo_1_c2[5] = 0
    else:
        variables_boton_estado[37] = True
        numero_boton[37].config(bg=color2)
        ritmo_1_c2[5] = 1

def boton_R1P7C2():
    global variables_boton_estado, ritmo_1_c2
    if variables_boton_estado[38]:
        variables_boton_estado[38] = False
        R1P7C2.config(bg="gray7")
        ritmo_1_c2[6] = 0
    else:
        variables_boton_estado[38] = True
        numero_boton[38].config(bg=color2)
        ritmo_1_c2[6] = 1

def boton_R1P8C2():
    global variables_boton_estado, ritmo_1_c2
    if variables_boton_estado[39]:
        variables_boton_estado[39] = False
        R1P8C2.config(bg="gray7")
        ritmo_1_c2[7] = 0
    else:
        variables_boton_estado[39] = True
        numero_boton[39].config(bg=color2)
        ritmo_1_c2[7] = 1

def boton_R2P1C2():
    global variables_boton_estado, ritmo_2_c2
    if variables_boton_estado[40]:
        variables_boton_estado[40] = False
        R2P1C2.config(bg="gray7")
        ritmo_2_c2[0] = 0
    else:
        variables_boton_estado[40] = True
        numero_boton[40].config(bg=color2)
        ritmo_2_c2[0] = 1

def boton_R2P2C2():
    global variables_boton_estado, ritmo_2_c2
    if variables_boton_estado[41]:
        variables_boton_estado[41] = False
        R2P2C2.config(bg="gray7")
        ritmo_2_c2[1] = 0
    else:
        variables_boton_estado[41] = True
        numero_boton[41].config(bg=color2)
        ritmo_2_c2[1] = 1

def boton_R2P3C2():
    global variables_boton_estado, ritmo_2_c2
    if variables_boton_estado[42]:
        variables_boton_estado[42] = False
        R2P3C2.config(bg="gray7")
        ritmo_2_c2[2] = 0
    else:
        variables_boton_estado[42] = True
        numero_boton[42].config(bg=color2)
        ritmo_2_c2[2] = 1

def boton_R2P4C2():
    global variables_boton_estado, ritmo_2_c2
    if variables_boton_estado[43]:
        variables_boton_estado[43] = False
        R2P4C2.config(bg="gray7")
        ritmo_2_c2[3] = 0
    else:
        variables_boton_estado[43] = True
        numero_boton[43].config(bg=color2)
        ritmo_2_c2[3] = 1

def boton_R2P5C2():
    global variables_boton_estado, ritmo_2_c2
    if variables_boton_estado[44]:
        variables_boton_estado[44] = False
        R2P5C2.config(bg="gray7")
        ritmo_2_c2[4] = 0
    else:
        variables_boton_estado[44] = True
        numero_boton[44].config(bg=color2)
        ritmo_2_c2[4] = 1

def boton_R2P6C2():
    global variables_boton_estado, ritmo_2_c2
    if variables_boton_estado[45]:
        variables_boton_estado[45] = False
        R2P6C2.config(bg="gray7")
        ritmo_2_c2[5] = 0
    else:
        variables_boton_estado[45] = True
        numero_boton[45].config(bg=color2)
        ritmo_2_c2[5] = 1

def boton_R2P7C2():
    global variables_boton_estado, ritmo_2_c2
    if variables_boton_estado[46]:
        variables_boton_estado[46] = False
        R2P7C2.config(bg="gray7")
        ritmo_2_c2[6] = 0
    else:
        variables_boton_estado[46] = True
        numero_boton[46].config(bg=color2)
        ritmo_2_c2[6] = 1

def boton_R2P8C2():
    global variables_boton_estado, ritmo_2_c2
    if variables_boton_estado[47]:
        variables_boton_estado[47] = False
        R2P8C2.config(bg="gray7")
        ritmo_2_c2[7] = 0
    else:
        variables_boton_estado[47] = True
        numero_boton[47].config(bg=color2)
        ritmo_2_c2[7] = 1

def boton_R3P1C2():
    global variables_boton_estado, ritmo_3_c2
    if variables_boton_estado[48]:
        variables_boton_estado[48] = False
        R3P1C2.config(bg="gray7")
        ritmo_3_c2[0] = 0
    else:
        variables_boton_estado[48] = True
        numero_boton[48].config(bg=color2)
        ritmo_3_c2[0] = 1

def boton_R3P2C2():
    global variables_boton_estado, ritmo_3_c2
    if variables_boton_estado[49]:
        variables_boton_estado[49] = False
        R3P2C2.config(bg="gray7")
        ritmo_3_c2[1] = 0
    else:
        variables_boton_estado[49] = True
        numero_boton[49].config(bg=color2)
        ritmo_3_c2[1] = 1

def boton_R3P3C2():
    global variables_boton_estado, ritmo_3_c2
    if variables_boton_estado[50]:
        variables_boton_estado[50] = False
        R3P3C2.config(bg="gray7")
        ritmo_3_c2[2] = 0
    else:
        variables_boton_estado[50] = True
        numero_boton[50].config(bg=color2)
        ritmo_3_c2[2] = 1

def boton_R3P4C2():
    global variables_boton_estado, ritmo_3_c2
    if variables_boton_estado[51]:
        variables_boton_estado[51] = False
        R3P4C2.config(bg="gray7")
        ritmo_3_c2[3] = 0
    else:
        variables_boton_estado[51] = True
        numero_boton[51].config(bg=color2)
        ritmo_3_c2[3] = 1

def boton_R3P5C2():
    global variables_boton_estado, ritmo_3_c2
    if variables_boton_estado[52]:
        variables_boton_estado[52] = False
        R3P5C2.config(bg="gray7")
        ritmo_3_c2[4] = 0
    else:
        variables_boton_estado[52] = True
        numero_boton[52].config(bg=color2)
        ritmo_3_c2[4] = 1

def boton_R3P6C2():
    global variables_boton_estado, ritmo_3_c2
    if variables_boton_estado[53]:
        variables_boton_estado[53] = False
        R3P6C2.config(bg="gray7")
        ritmo_3_c2[5] = 0
    else:
        variables_boton_estado[53] = True
        numero_boton[53].config(bg=color2)
        ritmo_3_c2[5] = 1

def boton_R3P7C2():
    global variables_boton_estado, ritmo_3_c2
    if variables_boton_estado[54]:
        variables_boton_estado[54] = False
        R3P7C2.config(bg="gray7")
        ritmo_3_c2[6] = 0
    else:
        variables_boton_estado[54] = True
        numero_boton[54].config(bg=color2)
        ritmo_3_c2[6] = 1

def boton_R3P8C2():
    global variables_boton_estado, ritmo_3_c2
    if variables_boton_estado[55]:
        variables_boton_estado[55] = False
        R3P8C2.config(bg="gray7")
        ritmo_3_c2[7] = 0
    else:
        variables_boton_estado[55] = True
        numero_boton[55].config(bg=color2)
        ritmo_3_c2[7] = 1

def boton_R4P1C2():
    global variables_boton_estado, ritmo_4_c2
    if variables_boton_estado[56]:
        variables_boton_estado[56] = False
        R4P1C2.config(bg="gray7")
        ritmo_4_c2[0] = 0
    else:
        variables_boton_estado[56] = True
        numero_boton[56].config(bg=color2)
        ritmo_4_c2[0] = 1

def boton_R4P2C2():
    global variables_boton_estado, ritmo_4_c2
    if variables_boton_estado[57]:
        variables_boton_estado[57] = False
        R4P2C2.config(bg="gray7")
        ritmo_4_c2[1] = 0
    else:
        variables_boton_estado[57] = True
        numero_boton[57].config(bg=color2)
        ritmo_4_c2[1] = 1

def boton_R4P3C2():
    global variables_boton_estado, ritmo_4_c2
    if variables_boton_estado[58]:
        variables_boton_estado[58] = False
        R4P3C2.config(bg="gray7")
        ritmo_4_c2[2] = 0
    else:
        variables_boton_estado[58] = True
        numero_boton[58].config(bg=color2)
        ritmo_4_c2[2] = 1

def boton_R4P4C2():
    global variables_boton_estado, ritmo_4_c2
    if variables_boton_estado[59]:
        variables_boton_estado[59] = False
        R4P4C2.config(bg="gray7")
        ritmo_4_c2[3] = 0
    else:
        variables_boton_estado[59] = True
        numero_boton[59].config(bg=color2)
        ritmo_4_c2[3] = 1

def boton_R4P5C2():
    global variables_boton_estado, ritmo_4_c2
    if variables_boton_estado[60]:
        variables_boton_estado[60] = False
        R4P5C2.config(bg="gray7")
        ritmo_4_c2[4] = 0
    else:
        variables_boton_estado[60] = True
        numero_boton[60].config(bg=color2)
        ritmo_4_c2[4] = 1

def boton_R4P6C2():
    global variables_boton_estado, ritmo_4_c2
    if variables_boton_estado[61]:
        variables_boton_estado[61] = False
        R4P6C2.config(bg="gray7")
        ritmo_4_c2[5] = 0
    else:
        variables_boton_estado[61] = True
        numero_boton[61].config(bg=color2)
        ritmo_4_c2[5] = 1

def boton_R4P7C2():
    global variables_boton_estado, ritmo_4_c2
    if variables_boton_estado[62]:
        variables_boton_estado[62] = False
        R4P7C2.config(bg="gray7")
        ritmo_4_c2[6] = 0
    else:
        variables_boton_estado[62] = True
        numero_boton[62].config(bg=color2)
        ritmo_4_c2[6] = 1

def boton_R4P8C2():
    global variables_boton_estado, ritmo_4_c2
    if variables_boton_estado[63]:
        variables_boton_estado[63] = False
        R4P8C2.config(bg="gray7")
        ritmo_4_c2[7] = 0
    else:
        variables_boton_estado[63] = True
        numero_boton[63].config(bg=color2)
        ritmo_4_c2[7] = 1

def boton_R1P1C3():
    global variables_boton_estado, ritmo_1_c3
    if variables_boton_estado[64]:
        variables_boton_estado[64] = False
        R1P1C3.config(bg="gray7")
        ritmo_1_c3[0] = 0
    else:
        variables_boton_estado[64] = True
        numero_boton[64].config(bg=color3)
        ritmo_1_c3[0] = 1

def boton_R1P2C3():
    global variables_boton_estado, ritmo_1_c3
    if variables_boton_estado[65]:
        variables_boton_estado[65] = False
        R1P2C3.config(bg="gray7")
        ritmo_1_c3[1] = 0
    else:
        variables_boton_estado[65] = True
        numero_boton[65].config(bg=color3)
        ritmo_1_c3[1] = 1

def boton_R1P3C3():
    global variables_boton_estado, ritmo_1_c3
    if variables_boton_estado[66]:
        variables_boton_estado[66] = False
        R1P3C3.config(bg="gray7")
        ritmo_1_c3[2] = 0
    else:
        variables_boton_estado[66] = True
        numero_boton[66].config(bg=color3)
        ritmo_1_c3[2] = 1

def boton_R1P4C3():
    global variables_boton_estado, ritmo_1_c3
    if variables_boton_estado[67]:
        variables_boton_estado[67] = False
        R1P4C3.config(bg="gray7")
        ritmo_1_c3[3] = 0
    else:
        variables_boton_estado[67] = True
        numero_boton[67].config(bg=color3)
        ritmo_1_c3[3] = 1

def boton_R1P5C3():
    global variables_boton_estado, ritmo_1_c3
    if variables_boton_estado[68]:
        variables_boton_estado[68] = False
        R1P5C3.config(bg="gray7")
        ritmo_1_c3[4] = 0
    else:
        variables_boton_estado[68] = True
        numero_boton[68].config(bg=color3)
        ritmo_1_c3[4] = 1

def boton_R1P6C3():
    global variables_boton_estado, ritmo_1_c3
    if variables_boton_estado[69]:
        variables_boton_estado[69] = False
        R1P6C3.config(bg="gray7")
        ritmo_1_c3[5] = 0
    else:
        variables_boton_estado[69] = True
        numero_boton[69].config(bg=color3)
        ritmo_1_c3[5] = 1

def boton_R1P7C3():
    global variables_boton_estado, ritmo_1_c3
    if variables_boton_estado[70]:
        variables_boton_estado[70] = False
        R1P7C3.config(bg="gray7")
        ritmo_1_c3[6] = 0
    else:
        variables_boton_estado[70] = True
        numero_boton[70].config(bg=color3)
        ritmo_1_c3[6] = 1

def boton_R1P8C3():
    global variables_boton_estado, ritmo_1_c3
    if variables_boton_estado[71]:
        variables_boton_estado[71] = False
        R1P8C3.config(bg="gray7")
        ritmo_1_c3[7] = 0
    else:
        variables_boton_estado[71] = True
        numero_boton[71].config(bg=color3)
        ritmo_1_c3[7] = 1

def boton_R2P1C3():
    global variables_boton_estado, ritmo_2_c3
    if variables_boton_estado[72]:
        variables_boton_estado[72] = False
        R2P1C3.config(bg="gray7")
        ritmo_2_c3[0] = 0
    else:
        variables_boton_estado[72] = True
        numero_boton[72].config(bg=color3)
        ritmo_2_c3[0] = 1

def boton_R2P2C3():
    global variables_boton_estado, ritmo_2_c3
    if variables_boton_estado[73]:
        variables_boton_estado[73] = False
        R2P2C3.config(bg="gray7")
        ritmo_2_c3[1] = 0
    else:
        variables_boton_estado[73] = True
        numero_boton[73].config(bg=color3)
        ritmo_2_c3[1] = 1

def boton_R2P3C3():
    global variables_boton_estado, ritmo_2_c3
    if variables_boton_estado[74]:
        variables_boton_estado[74] = False
        R2P3C3.config(bg="gray7")
        ritmo_2_c3[2] = 0
    else:
        variables_boton_estado[74] = True
        numero_boton[74].config(bg=color3)
        ritmo_2_c3[2] = 1

def boton_R2P4C3():
    global variables_boton_estado, ritmo_2_c3
    if variables_boton_estado[75]:
        variables_boton_estado[75] = False
        R2P4C3.config(bg="gray7")
        ritmo_2_c3[3] = 0
    else:
        variables_boton_estado[75] = True
        numero_boton[75].config(bg=color3)
        ritmo_2_c3[3] = 1

def boton_R2P5C3():
    global variables_boton_estado, ritmo_2_c3
    if variables_boton_estado[76]:
        variables_boton_estado[76] = False
        R2P5C3.config(bg="gray7")
        ritmo_2_c3[4] = 0
    else:
        variables_boton_estado[76] = True
        numero_boton[76].config(bg=color3)
        ritmo_2_c3[4] = 1

def boton_R2P6C3():
    global variables_boton_estado, ritmo_2_c3
    if variables_boton_estado[77]:
        variables_boton_estado[77] = False
        R2P6C3.config(bg="gray7")
        ritmo_2_c3[5] = 0
    else:
        variables_boton_estado[77] = True
        numero_boton[77].config(bg=color3)
        ritmo_2_c3[5] = 1

def boton_R2P7C3():
    global variables_boton_estado, ritmo_2_c3
    if variables_boton_estado[78]:
        variables_boton_estado[78] = False
        R2P7C3.config(bg="gray7")
        ritmo_2_c3[6] = 0
    else:
        variables_boton_estado[78] = True
        numero_boton[78].config(bg=color3)
        ritmo_2_c3[6] = 1

def boton_R2P8C3():
    global variables_boton_estado, ritmo_2_c3
    if variables_boton_estado[79]:
        variables_boton_estado[79] = False
        R2P8C3.config(bg="gray7")
        ritmo_2_c3[7] = 0
    else:
        variables_boton_estado[79] = True
        numero_boton[79].config(bg=color3)
        ritmo_2_c3[7] = 1

def boton_R3P1C3():
    global variables_boton_estado, ritmo_3_c3
    if variables_boton_estado[80]:
        variables_boton_estado[80] = False
        R3P1C3.config(bg="gray7")
        ritmo_3_c3[0] = 0
    else:
        variables_boton_estado[80] = True
        numero_boton[80].config(bg=color3)
        ritmo_3_c3[0] = 1

def boton_R3P2C3():
    global variables_boton_estado, ritmo_3_c3
    if variables_boton_estado[81]:
        variables_boton_estado[81] = False
        R3P2C3.config(bg="gray7")
        ritmo_3_c3[1] = 0
    else:
        variables_boton_estado[81] = True
        numero_boton[81].config(bg=color3)
        ritmo_3_c3[1] = 1

def boton_R3P3C3():
    global variables_boton_estado, ritmo_3_c3
    if variables_boton_estado[82]:
        variables_boton_estado[82] = False
        R3P3C3.config(bg="gray7")
        ritmo_3_c3[2] = 0
    else:
        variables_boton_estado[82] = True
        numero_boton[82].config(bg=color3)
        ritmo_3_c3[2] = 1

def boton_R3P4C3():
    global variables_boton_estado, ritmo_3_c3
    if variables_boton_estado[83]:
        variables_boton_estado[83] = False
        R3P4C3.config(bg="gray7")
        ritmo_3_c3[3] = 0
    else:
        variables_boton_estado[83] = True
        numero_boton[83].config(bg=color3)
        ritmo_3_c3[3] = 1

def boton_R3P5C3():
    global variables_boton_estado, ritmo_3_c3
    if variables_boton_estado[84]:
        variables_boton_estado[84] = False
        R3P5C3.config(bg="gray7")
        ritmo_3_c3[4] = 0
    else:
        variables_boton_estado[84] = True
        numero_boton[84].config(bg=color3)
        ritmo_3_c3[4] = 1

def boton_R3P6C3():
    global variables_boton_estado, ritmo_3_c3
    if variables_boton_estado[85]:
        variables_boton_estado[85] = False
        R3P6C3.config(bg="gray7")
        ritmo_3_c3[5] = 0
    else:
        variables_boton_estado[85] = True
        numero_boton[85].config(bg=color3)
        ritmo_3_c3[5] = 1

def boton_R3P7C3():
    global variables_boton_estado, ritmo_3_c3
    if variables_boton_estado[86]:
        variables_boton_estado[86] = False
        R3P7C3.config(bg="gray7")
        ritmo_3_c3[6] = 0
    else:
        variables_boton_estado[86] = True
        numero_boton[86].config(bg=color3)
        ritmo_3_c3[6] = 1

def boton_R3P8C3():
    global variables_boton_estado, ritmo_3_c3
    if variables_boton_estado[87]:
        variables_boton_estado[87] = False
        R3P8C3.config(bg="gray7")
        ritmo_3_c3[7] = 0
    else:
        variables_boton_estado[87] = True
        numero_boton[87].config(bg=color3)
        ritmo_3_c3[7] = 1

def boton_R4P1C3():
    global variables_boton_estado, ritmo_4_c3
    if variables_boton_estado[88]:
        variables_boton_estado[88] = False
        R4P1C3.config(bg="gray7")
        ritmo_4_c3[0] = 0
    else:
        variables_boton_estado[88] = True
        numero_boton[88].config(bg=color3)
        ritmo_4_c3[0] = 1

def boton_R4P2C3():
    global variables_boton_estado, ritmo_4_c3
    if variables_boton_estado[89]:
        variables_boton_estado[89] = False
        R4P2C3.config(bg="gray7")
        ritmo_4_c3[1] = 0
    else:
        variables_boton_estado[89] = True
        numero_boton[89].config(bg=color3)
        ritmo_4_c3[1] = 1

def boton_R4P3C3():
    global variables_boton_estado, ritmo_4_c3
    if variables_boton_estado[90]:
        variables_boton_estado[90] = False
        R4P3C3.config(bg="gray7")
        ritmo_4_c3[2] = 0
    else:
        variables_boton_estado[90] = True
        numero_boton[90].config(bg=color3)
        ritmo_4_c3[2] = 1

def boton_R4P4C3():
    global variables_boton_estado, ritmo_4_c3
    if variables_boton_estado[91]:
        variables_boton_estado[91] = False
        R4P4C3.config(bg="gray7")
        ritmo_4_c3[3] = 0
    else:
        variables_boton_estado[91] = True
        numero_boton[91].config(bg=color3)
        ritmo_4_c3[3] = 1

def boton_R4P5C3():
    global variables_boton_estado, ritmo_4_c3
    if variables_boton_estado[92]:
        variables_boton_estado[92] = False
        R4P5C3.config(bg="gray7")
        ritmo_4_c3[4] = 0
    else:
        variables_boton_estado[92] = True
        numero_boton[92].config(bg=color3)
        ritmo_4_c3[4] = 1

def boton_R4P6C3():
    global variables_boton_estado, ritmo_4_c3
    if variables_boton_estado[93]:
        variables_boton_estado[93] = False
        R4P6C3.config(bg="gray7")
        ritmo_4_c3[5] = 0
    else:
        variables_boton_estado[93] = True
        numero_boton[93].config(bg=color3)
        ritmo_4_c3[5] = 1

def boton_R4P7C3():
    global variables_boton_estado, ritmo_4_c3
    if variables_boton_estado[94]:
        variables_boton_estado[94] = False
        R4P7C3.config(bg="gray7")
        ritmo_4_c3[6] = 0
    else:
        variables_boton_estado[94] = True
        numero_boton[94].config(bg=color3)
        ritmo_4_c3[6] = 1

def boton_R4P8C3():
    global variables_boton_estado, ritmo_4_c3
    if variables_boton_estado[95]:
        variables_boton_estado[95] = False
        R4P8C3.config(bg="gray7")
        ritmo_4_c3[7] = 0
    else:
        variables_boton_estado[95] = True
        numero_boton[95].config(bg=color3)
        ritmo_4_c3[7] = 1

def boton_R1P1C4():
    global variables_boton_estado, ritmo_1_c4
    if variables_boton_estado[96]:
        variables_boton_estado[96] = False
        R1P1C4.config(bg="gray7")
        ritmo_1_c4[0] = 0
    else:
        variables_boton_estado[96] = True
        numero_boton[96].config(bg=color4)
        ritmo_1_c4[0] = 1

def boton_R1P2C4():
    global variables_boton_estado, ritmo_1_c4
    if variables_boton_estado[97]:
        variables_boton_estado[97] = False
        R1P2C4.config(bg="gray7")
        ritmo_1_c4[1] = 0
    else:
        variables_boton_estado[97] = True
        numero_boton[97].config(bg=color4)
        ritmo_1_c4[1] = 1

def boton_R1P3C4():
    global variables_boton_estado, ritmo_1_c4
    if variables_boton_estado[98]:
        variables_boton_estado[98] = False
        R1P3C4.config(bg="gray7")
        ritmo_1_c4[2] = 0
    else:
        variables_boton_estado[98] = True
        numero_boton[98].config(bg=color4)
        ritmo_1_c4[2] = 1

def boton_R1P4C4():
    global variables_boton_estado, ritmo_1_c4
    if variables_boton_estado[99]:
        variables_boton_estado[99] = False
        R1P4C4.config(bg="gray7")
        ritmo_1_c4[3] = 0
    else:
        variables_boton_estado[99] = True
        numero_boton[99].config(bg=color4)
        ritmo_1_c4[3] = 1

def boton_R1P5C4():
    global variables_boton_estado, ritmo_1_c4
    if variables_boton_estado[100]:
        variables_boton_estado[100] = False
        R1P5C4.config(bg="gray7")
        ritmo_1_c4[4] = 0
    else:
        variables_boton_estado[100] = True
        numero_boton[100].config(bg=color4)
        ritmo_1_c4[4] = 1

def boton_R1P6C4():
    global variables_boton_estado, ritmo_1_c4
    if variables_boton_estado[101]:
        variables_boton_estado[101] = False
        R1P6C4.config(bg="gray7")
        ritmo_1_c4[5] = 0
    else:
        variables_boton_estado[101] = True
        numero_boton[101].config(bg=color4)
        ritmo_1_c4[5] = 1

def boton_R1P7C4():
    global variables_boton_estado, ritmo_1_c4
    if variables_boton_estado[102]:
        variables_boton_estado[102] = False
        R1P7C4.config(bg="gray7")
        ritmo_1_c4[6] = 0
    else:
        variables_boton_estado[102] = True
        numero_boton[102].config(bg=color4)
        ritmo_1_c4[6] = 1

def boton_R1P8C4():
    global variables_boton_estado, ritmo_1_c4
    if variables_boton_estado[103]:
        variables_boton_estado[103] = False
        R1P8C4.config(bg="gray7")
        ritmo_1_c4[7] = 0
    else:
        variables_boton_estado[103] = True
        numero_boton[103].config(bg=color4)
        ritmo_1_c4[7] = 1

def boton_R2P1C4():
    global variables_boton_estado, ritmo_2_c4
    if variables_boton_estado[104]:
        variables_boton_estado[104] = False
        R2P1C4.config(bg="gray7")
        ritmo_2_c4[0] = 0
    else:
        variables_boton_estado[104] = True
        numero_boton[104].config(bg=color4)
        ritmo_2_c4[0] = 1

def boton_R2P2C4():
    global variables_boton_estado, ritmo_2_c4
    if variables_boton_estado[105]:
        variables_boton_estado[105] = False
        R2P2C4.config(bg="gray7")
        ritmo_2_c4[1] = 0
    else:
        variables_boton_estado[105] = True
        numero_boton[105].config(bg=color4)
        ritmo_2_c4[1] = 1

def boton_R2P3C4():
    global variables_boton_estado, ritmo_2_c4
    if variables_boton_estado[106]:
        variables_boton_estado[106] = False
        R2P3C4.config(bg="gray7")
        ritmo_2_c4[2] = 0
    else:
        variables_boton_estado[106] = True
        numero_boton[106].config(bg=color4)
        ritmo_2_c4[2] = 1

def boton_R2P4C4():
    global variables_boton_estado, ritmo_2_c4
    if variables_boton_estado[107]:
        variables_boton_estado[107] = False
        R2P4C4.config(bg="gray7")
        ritmo_2_c4[3] = 0
    else:
        variables_boton_estado[107] = True
        numero_boton[107].config(bg=color4)
        ritmo_2_c4[3] = 1

def boton_R2P5C4():
    global variables_boton_estado, ritmo_2_c4
    if variables_boton_estado[108]:
        variables_boton_estado[108] = False
        R2P5C4.config(bg="gray7")
        ritmo_2_c4[4] = 0
    else:
        variables_boton_estado[108] = True
        numero_boton[108].config(bg=color4)
        ritmo_2_c4[4] = 1

def boton_R2P6C4():
    global variables_boton_estado, ritmo_2_c4
    if variables_boton_estado[109]:
        variables_boton_estado[109] = False
        R2P6C4.config(bg="gray7")
        ritmo_2_c4[5] = 0
    else:
        variables_boton_estado[109] = True
        numero_boton[109].config(bg=color4)
        ritmo_2_c4[5] = 1

def boton_R2P7C4():
    global variables_boton_estado, ritmo_2_c4
    if variables_boton_estado[110]:
        variables_boton_estado[110] = False
        R2P7C4.config(bg="gray7")
        ritmo_2_c4[6] = 0
    else:
        variables_boton_estado[110] = True
        numero_boton[110].config(bg=color4)
        ritmo_2_c4[6] = 1

def boton_R2P8C4():
    global variables_boton_estado, ritmo_2_c4
    if variables_boton_estado[111]:
        variables_boton_estado[111] = False
        R2P8C4.config(bg="gray7")
        ritmo_2_c4[7] = 0
    else:
        variables_boton_estado[111] = True
        numero_boton[111].config(bg=color4)
        ritmo_2_c4[7] = 1

def boton_R3P1C4():
    global variables_boton_estado, ritmo_3_c4
    if variables_boton_estado[112]:
        variables_boton_estado[112] = False
        R3P1C4.config(bg="gray7")
        ritmo_3_c4[0] = 0
    else:
        variables_boton_estado[112] = True
        numero_boton[112].config(bg=color4)
        ritmo_3_c4[0] = 1

def boton_R3P2C4():
    global variables_boton_estado, ritmo_3_c4
    if variables_boton_estado[113]:
        variables_boton_estado[113] = False
        R3P2C4.config(bg="gray7")
        ritmo_3_c4[1] = 0
    else:
        variables_boton_estado[113] = True
        numero_boton[113].config(bg=color4)
        ritmo_3_c4[1] = 1

def boton_R3P3C4():
    global variables_boton_estado, ritmo_3_c4
    if variables_boton_estado[114]:
        variables_boton_estado[114] = False
        R3P3C4.config(bg="gray7")
        ritmo_3_c4[2] = 0
    else:
        variables_boton_estado[114] = True
        numero_boton[114].config(bg=color4)
        ritmo_3_c4[2] = 1

def boton_R3P4C4():
    global variables_boton_estado, ritmo_3_c4
    if variables_boton_estado[115]:
        variables_boton_estado[115] = False
        R3P4C4.config(bg="gray7")
        ritmo_3_c4[3] = 0
    else:
        variables_boton_estado[115] = True
        numero_boton[115].config(bg=color4)
        ritmo_3_c4[3] = 1

def boton_R3P5C4():
    global variables_boton_estado, ritmo_3_c4
    if variables_boton_estado[116]:
        variables_boton_estado[116] = False
        R3P5C4.config(bg="gray7")
        ritmo_3_c4[4] = 0
    else:
        variables_boton_estado[116] = True
        numero_boton[116].config(bg=color4)
        ritmo_3_c4[4] = 1

def boton_R3P6C4():
    global variables_boton_estado, ritmo_3_c4
    if variables_boton_estado[117]:
        variables_boton_estado[117] = False
        R3P6C4.config(bg="gray7")
        ritmo_3_c4[5] = 0
    else:
        variables_boton_estado[117] = True
        numero_boton[117].config(bg=color4)
        ritmo_3_c4[5] = 1

def boton_R3P7C4():
    global variables_boton_estado, ritmo_3_c4
    if variables_boton_estado[118]:
        variables_boton_estado[118] = False
        R3P7C4.config(bg="gray7")
        ritmo_3_c4[6] = 0
    else:
        variables_boton_estado[118] = True
        numero_boton[118].config(bg=color4)
        ritmo_3_c4[6] = 1

def boton_R3P8C4():
    global variables_boton_estado, ritmo_3_c4
    if variables_boton_estado[119]:
        variables_boton_estado[119] = False
        R3P8C4.config(bg="gray7")
        ritmo_3_c4[7] = 0
    else:
        variables_boton_estado[119] = True
        numero_boton[119].config(bg=color4)
        ritmo_3_c4[7] = 1

def boton_R4P1C4():
    global variables_boton_estado, ritmo_4_c4
    if variables_boton_estado[120]:
        variables_boton_estado[120] = False
        R4P1C4.config(bg="gray7")
        ritmo_4_c4[0] = 0
    else:
        variables_boton_estado[120] = True
        numero_boton[120].config(bg=color4)
        ritmo_4_c4[0] = 1

def boton_R4P2C4():
    global variables_boton_estado, ritmo_4_c4
    if variables_boton_estado[121]:
        variables_boton_estado[121] = False
        R4P2C4.config(bg="gray7")
        ritmo_4_c4[1] = 0
    else:
        variables_boton_estado[121] = True
        numero_boton[121].config(bg=color4)
        ritmo_4_c4[1] = 1

def boton_R4P3C4():
    global variables_boton_estado, ritmo_4_c4
    if variables_boton_estado[122]:
        variables_boton_estado[122] = False
        R4P3C4.config(bg="gray7")
        ritmo_4_c4[2] = 0
    else:
        variables_boton_estado[122] = True
        numero_boton[122].config(bg=color4)
        ritmo_4_c4[2] = 1

def boton_R4P4C4():
    global variables_boton_estado, ritmo_4_c4
    if variables_boton_estado[123]:
        variables_boton_estado[123] = False
        R4P4C4.config(bg="gray7")
        ritmo_4_c4[3] = 0
    else:
        variables_boton_estado[123] = True
        numero_boton[123].config(bg=color4)
        ritmo_4_c4[3] = 1

def boton_R4P5C4():
    global variables_boton_estado, ritmo_4_c4
    if variables_boton_estado[124]:
        variables_boton_estado[124] = False
        R4P5C4.config(bg="gray7")
        ritmo_4_c4[4] = 0
    else:
        variables_boton_estado[124] = True
        numero_boton[124].config(bg=color4)
        ritmo_4_c4[4] = 1

def boton_R4P6C4():
    global variables_boton_estado, ritmo_4_c4
    if variables_boton_estado[125]:
        variables_boton_estado[125] = False
        R4P6C4.config(bg="gray7")
        ritmo_4_c4[5] = 0
    else:
        variables_boton_estado[125] = True
        numero_boton[125].config(bg=color4)
        ritmo_4_c4[5] = 1

def boton_R4P7C4():
    global variables_boton_estado, ritmo_4_c4
    if variables_boton_estado[126]:
        variables_boton_estado[126] = False
        R4P7C4.config(bg="gray7")
        ritmo_4_c4[6] = 0
    else:
        variables_boton_estado[126] = True
        numero_boton[126].config(bg=color4)
        ritmo_4_c4[6] = 1

def boton_R4P8C4():
    global variables_boton_estado, ritmo_4_c4
    if variables_boton_estado[127]:
        variables_boton_estado[127] = False
        R4P8C4.config(bg="gray7")
        ritmo_4_c4[7] = 0
    else:
        variables_boton_estado[127] = True
        numero_boton[127].config(bg=color4)
        ritmo_4_c4[7] = 1


def fuerza_bruta():
    hola

def fuerza_bruta_ritmo1():
    caja_fuerza.set

def fuerza_bruta_ritmo2():
    tex

def fuerza_bruta_ritmo3():
    tex

def fuerza_bruta_ritmo4():
    tex



#Interfaz

raiz = Tk()
raiz.title("Symmetric Byte - by Brick Briceño")
raiz.config(bg="black")
#raiz.iconbitmap('br.ico')

raiz.geometry("1060x560")
raiz.resizable (0,0)

#Ritmo Reloj

reloj_ritmo = Frame(raiz, bg="gray12")
reloj_ritmo.pack(side="right", anchor="n")
reloj_ritmo.place(x=500, y=18, width=520, height=520)

canvas = Canvas(reloj_ritmo, width="490", height="490", bg="black", bd=10)
canvas.grid(padx=5, pady=5)

canvas.create_oval(15, 15, 500, 500, fill="gray2", outline="gray5", width=5)
#canvas.create_oval(240,240,250,250, fill='snow' , outline ='black', width=1)

numeros = [16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]

for i in range(0, 16):
    canvas.create_text(257-230*sin(((i+1)*2*pi)/16), 257-230*cos(((i+1)*2*pi)/16), text= numeros[i], font=('Arial',12, 'bold'), fill ="snow")
for x in range(16):
    canvas.create_text(257-210*sin(((x+1)*2*pi)/16), 257-210*cos(((x+1)*2*pi)/16), text= '•', font=('Arial',25, 'bold'), fill=color1)

canvas.create_line(257, 257, 257 + 16*sin(radians(1)), 100 - 16*cos(radians(1)), fill='red',width=9,arrow= LAST)

#Meter datos y controles:

datos = Frame(raiz, bg="black")
datos.pack(side="left", anchor="n")
datos.place(x=18, y=18)

botones = Frame(raiz, bg="black", width=480, height=480)
botones.pack(side="left", anchor="n")
botones.place(x=18, y=150)

inEu1D = StringVar()
inEu1T = Entry(datos, font=(24), width=10, textvariable=inEu1D)
inEu1T.grid(row=0, column=1)
inEu1T.config(justify="center", bg="gray5", fg="snow")
inEu1D.set("4,8")

inEu2D = StringVar()
inEu2T = Entry(datos, font=(24), width=10, textvariable=inEu2D)
inEu2T.grid(row=1, column=1)
inEu2T.config(justify="center", bg="gray5", fg="snow")
inEu2D.set("2,8")

inEu3D = StringVar()
inEu3T = Entry(datos, font=(24), width=10, textvariable=inEu3D)
inEu3T.grid(row=2, column=1)
inEu3T.config(justify="center", bg="gray5", fg="snow")
inEu3D.set("2,8")

inEu4D = StringVar()
inEu4T = Entry(datos, font=(24), width=10, textvariable=inEu4D)
inEu4T.grid(row=3, column=1)
inEu4T.config(justify="center", bg="gray5", fg="snow")
inEu4D.set("8,8")

TempoD = StringVar()
inTempo = Entry(datos, font=(24), width=10, textvariable=TempoD)
inTempo.grid(row=4, column=1)
inTempo.config(justify="center", bg="gray5", fg="snow")
TempoD.set(128)

labelEu1T = Label(datos, text="Ritmo 1: ", font=(24))
labelEu1T.grid(row=0, column=0, sticky="e")
labelEu1T.config(justify="center", bg="gray5", fg="snow")

labelEu2T = Label(datos, text="Ritmo 2: ", font=(24))
labelEu2T.grid(row=1, column=0, sticky="e")
labelEu2T.config(justify="center", bg="gray5", fg="snow")

labelEu3T = Label(datos, text="Ritmo 3: ", font=(24))
labelEu3T.grid(row=2, column=0, sticky="e")
labelEu3T.config(justify="center", bg="gray5", fg="snow")

labelEu4T = Label(datos, text="Ritmo 4: ", font=(24))
labelEu4T.grid(row=3, column=0, sticky="e")
labelEu4T.config(justify="center", bg="gray5", fg="snow")

labelTempo = Label(datos, text=" Tempo: ", font=(24))
labelTempo.grid(row=4, column=0, sticky="e")
labelTempo.config(justify="center", bg="gray5", fg="snow")

#Botones
botonPausar=Button(botones, command=Pausar, text="Pause", font=(22))
botonPausar.grid(row=2, column=0)
botonPausar.config(bg="gray5", fg="snow", font=(22))
botonPlay=Button(botones, command=Play, text="Play")
botonPlay.grid(row=2, column=1)
botonPlay.config(bg="gray8", fg="snow", font=(22))
botonRevertir=Button(botones, command=Revertir, text="Revertir")
botonRevertir.grid(row=2, column=3)
botonRevertir.config(bg="gray5", fg="snow", font=(22))
botonGuardar=Button(botones, command=Guardar, text="Guardar Ritmo")
botonGuardar.grid(row=2, column=4)
botonGuardar.config(bg="gray5", fg="snow", font=(22))
botonAleatorio=Button(botones, command=ramdon_todo, text="Aleatorio")
botonAleatorio.grid(row=2, column=5)
botonAleatorio.config(bg="gray5", fg="snow", font=(22))

#Fuerza bruta

fuerza_brutaR1=Button(datos, command=fuerza_bruta_ritmo1, text="Fuerza Bruta")
fuerza_brutaR1.grid(row=0, column=10)
fuerza_brutaR1.config(bg="gray7", fg="snow")
fuerza_brutaR2=Button(datos, command=fuerza_bruta_ritmo2, text="Fuerza Bruta")
fuerza_brutaR2.grid(row=1, column=10)
fuerza_brutaR2.config(bg="gray7", fg="snow")
fuerza_brutaR3=Button(datos, command=fuerza_bruta_ritmo3, text="Fuerza Bruta")
fuerza_brutaR3.grid(row=2, column=10)
fuerza_brutaR3.config(bg="gray7", fg="snow")
fuerza_brutaR4=Button(datos, command=fuerza_bruta_ritmo4, text="Fuerza Bruta")
fuerza_brutaR4.grid(row=3, column=10)
fuerza_brutaR4.config(bg="gray7", fg="snow")

caja_fuerza = Frame(raiz, bg="gray12")
caja_fuerza.pack(side="right", anchor="n")
caja_fuerza.place(x=18, y=420)

texto = Text(caja_fuerza)
texto.pack(fill="both", expand=1)
texto.config(width="45", height="5", bg="gray3", fg="snow", bd=0, padx=4, pady=4, font=("Consolas",14))
texto.insert("insert", "Bienvenido ^^\nuwu")#este es el comando

#Enviar a

enviar_a = Frame(raiz, bg="black")
enviar_a.pack(side="left", anchor="n")
enviar_a.place(x=298, y=123)

labelEnviar = Label(enviar_a, text="Enviar a:", font=(22))
labelEnviar.grid(row=2, column=6, sticky="e")
labelEnviar.config(justify="center", bg="gray5", fg="snow")

#Enviar a
botonEnviar=Button(enviar_a, command=enviar_c1, text="C1")
botonEnviar.grid(row=2, column=7)
botonEnviar.config(bg=color1, fg="snow")

botonEnviar=Button(enviar_a, command=enviar_c2, text="C2")
botonEnviar.grid(row=2, column=8)
botonEnviar.config(bg=color2, fg="snow")

botonEnviar=Button(enviar_a, command=enviar_c3, text="C3")
botonEnviar.grid(row=2, column=9)
botonEnviar.config(bg=color3, fg="snow")

botonEnviar=Button(enviar_a, command=enviar_c4, text="C4")
botonEnviar.grid(row=2, column=10)
botonEnviar.config(bg=color4, fg="snow")


botonEu1=Button(datos, command=Eu1, text="Cambiar")
botonEu1.grid(row=0, column=2)
botonEu1.config(bg="gray5", fg="snow")
botonEu2=Button(datos, command=Eu2, text="Cambiar")
botonEu2.grid(row=1, column=2)
botonEu2.config(bg="gray5", fg="snow")
botonEu3=Button(datos, command=Eu3, text="Cambiar")
botonEu3.grid(row=2, column=2)
botonEu3.config(bg="gray5", fg="snow")
botonEu4=Button(datos, command=Eu4, text="Cambiar")
botonEu4.grid(row=3, column=2)
botonEu4.config(bg="gray5", fg="snow")

botonTempo=Button(datos, command=redondear_tempo, text="Redondear", width=7)
botonTempo.grid(row=4, column=2)
botonTempo.config(bg="gray5", fg="snow")

manualTempo=Button(datos, command=lambda:tempo_manual(None), text="m")
manualTempo.grid(row=4, column=3)
manualTempo.config(bg="slateblue4", fg="black", width="1", height="1")
aleatrioTempo=Button(datos, command=ramdon_tempo, text="A")
aleatrioTempo.grid(row=4, column=4)
aleatrioTempo.config(bg="gray5", fg="snow", width="2")

claqueta=Button(datos, command=claqueta, text="*")
claqueta.grid(row=4, column=5)
claqueta.config(bg="gray10", fg="snow")

#Mute
mute1=Button(datos, command=mute1, text="M")
mute1.grid(row=0, column=4)
mute1.config(bg="gray6", fg="snow")
mute2=Button(datos, command=mute2, text="M")
mute2.grid(row=1, column=4)
mute2.config(bg="gray6", fg="snow")
mute3=Button(datos, command=mute3, text="M")
mute3.grid(row=2, column=4)
mute3.config(bg="gray6", fg="snow")
mute4=Button(datos, command=mute4, text="M")
mute4.grid(row=3, column=4)
mute4.config(bg="gray6", fg="snow")

#Revertir
revertir1=Button(datos, command=Revertir1, text="R")
revertir1.grid(row=0, column=3)
revertir1.config(bg="gray7", fg="snow")
revertir2=Button(datos, command=Revertir2, text="R")
revertir2.grid(row=1, column=3)
revertir2.config(bg="gray7", fg="snow")
revertir3=Button(datos, command=Revertir3, text="R")
revertir3.grid(row=2, column=3)
revertir3.config(bg="gray7", fg="snow")
revertir4=Button(datos, command=Revertir4, text="R")
revertir4.grid(row=3, column=3)
revertir4.config(bg="gray7", fg="snow")

#Mover
mover_izquierda1=Button(datos, command=mover_1_izquierda, text="<")
mover_izquierda1.grid(row=0, column=5)
mover_izquierda1.config(bg="gray7", fg="snow")
mover_izquierda2=Button(datos, command=mover_2_izquierda, text="<")
mover_izquierda2.grid(row=1, column=5)
mover_izquierda2.config(bg="gray7", fg="snow")
mover_izquierda3=Button(datos, command=mover_3_izquierda, text="<")
mover_izquierda3.grid(row=2, column=5)
mover_izquierda3.config(bg="gray7", fg="snow")
mover_izquierda4=Button(datos, command=mover_4_izquierda, text="<")
mover_izquierda4.grid(row=3, column=5)
mover_izquierda4.config(bg="gray7", fg="snow")

mover_derecha1=Button(datos, command=mover_1_derecha, text=">")
mover_derecha1.grid(row=0, column=6)
mover_derecha1.config(bg="gray7", fg="snow")
mover_derecha2=Button(datos, command=mover_2_derecha, text=">")
mover_derecha2.grid(row=1, column=6)
mover_derecha2.config(bg="gray7", fg="snow")
mover_derecha3=Button(datos, command=mover_3_derecha, text=">")
mover_derecha3.grid(row=2, column=6)
mover_derecha3.config(bg="gray7", fg="snow")
mover_derecha4=Button(datos, command=mover_4_derecha, text=">")
mover_derecha4.grid(row=3, column=6)
mover_derecha4.config(bg="gray7", fg="snow")

#aleatorio 1
mover_derecha1=Button(datos, command=ramdon1_r1, text="A1")
mover_derecha1.grid(row=0, column=7)
mover_derecha1.config(bg="gray7", fg="snow")
mover_derecha2=Button(datos, command=ramdon1_r2, text="A1")
mover_derecha2.grid(row=1, column=7)
mover_derecha2.config(bg="gray7", fg="snow")
mover_derecha3=Button(datos, command=ramdon1_r3, text="A1")
mover_derecha3.grid(row=2, column=7)
mover_derecha3.config(bg="gray7", fg="snow")
mover_derecha4=Button(datos, command=ramdon1_r4, text="A1")
mover_derecha4.grid(row=3, column=7)
mover_derecha4.config(bg="gray7", fg="snow")

#aleatorio 2
mover_derecha1=Button(datos, command=ramdon2_r1, text="A2")
mover_derecha1.grid(row=0, column=8)
mover_derecha1.config(bg="gray7", fg="snow")
mover_derecha2=Button(datos, command=ramdon2_r2, text="A2")
mover_derecha2.grid(row=1, column=8)
mover_derecha2.config(bg="gray7", fg="snow")
mover_derecha3=Button(datos, command=ramdon2_r3, text="A2")
mover_derecha3.grid(row=2, column=8)
mover_derecha3.config(bg="gray7", fg="snow")
mover_derecha4=Button(datos, command=ramdon2_r4, text="A2")
mover_derecha4.grid(row=3, column=8)
mover_derecha4.config(bg="gray7", fg="snow")

#aleatorio 3
mover_derecha1=Button(datos, command=ramdon3_r1, text="A3")
mover_derecha1.grid(row=0, column=9)
mover_derecha1.config(bg="gray7", fg="snow")
mover_derecha2=Button(datos, command=ramdon3_r2, text="A3")
mover_derecha2.grid(row=1, column=9)
mover_derecha2.config(bg="gray7", fg="snow")
mover_derecha3=Button(datos, command=ramdon3_r3, text="A3")
mover_derecha3.grid(row=2, column=9)
mover_derecha3.config(bg="gray7", fg="snow")
mover_derecha4=Button(datos, command=ramdon3_r4, text="A3")
mover_derecha4.grid(row=3, column=9)
mover_derecha4.config(bg="gray7", fg="snow")

#Editor de ritmos:

editor = Frame(raiz, bg="black")
editor.pack(side="left", anchor="n")
editor.place(x=18, y=200)


#Pertitura 1
labelP1R = Label(editor, text="R1 P1:", font=(24))
labelP1R.grid(row=0, column=0)
labelP1R.config(justify="center", bg="gray5", fg="snow")

labelP1R = Label(editor, text="R2 P1:", font=(24))
labelP1R.grid(row=1, column=0)
labelP1R.config(justify="center", bg="gray5", fg="snow")

labelP1R = Label(editor, text="R3 P1:", font=(24))
labelP1R.grid(row=2, column=0)
labelP1R.config(justify="center", bg="gray5", fg="snow")

labelP1R = Label(editor, text="R4 P1:", font=(24))
labelP1R.grid(row=3, column=0)
labelP1R.config(justify="center", bg="gray5", fg="snow")

#Pertitura 2
labelP1R = Label(editor, text="R1 P2:", font=(24))
labelP1R.grid(row=0, column=9)
labelP1R.config(justify="center", bg="gray5", fg="snow")

labelP1R = Label(editor, text="R2 P2:", font=(24))
labelP1R.grid(row=1, column=9)
labelP1R.config(justify="center", bg="gray5", fg="snow")

labelP1R = Label(editor, text="R3 P2:", font=(24))
labelP1R.grid(row=2, column=9)
labelP1R.config(justify="center", bg="gray5", fg="snow")

labelP1R = Label(editor, text="R4 P2:", font=(24))
labelP1R.grid(row=3, column=9)
labelP1R.config(justify="center", bg="gray5", fg="snow")

#Pertitura 3
labelP1R = Label(editor, text="R1 P3:", font=(24))
labelP1R.grid(row=4, column=0)
labelP1R.config(justify="center", bg="gray5", fg="snow")

labelP1R = Label(editor, text="R2 P3:", font=(24))
labelP1R.grid(row=5, column=0)
labelP1R.config(justify="center", bg="gray5", fg="snow")

labelP1R = Label(editor, text="R3 P3:", font=(24))
labelP1R.grid(row=6, column=0)
labelP1R.config(justify="center", bg="gray5", fg="snow")

labelP1R = Label(editor, text="R4 P3:", font=(24))
labelP1R.grid(row=7, column=0)
labelP1R.config(justify="center", bg="gray5", fg="snow")

#Pertitura 4
labelP1R = Label(editor, text="R1 P4:", font=(24))
labelP1R.grid(row=4, column=9)
labelP1R.config(justify="center", bg="gray5", fg="snow")

labelP1R = Label(editor, text="R2 P4:", font=(24))
labelP1R.grid(row=5, column=9)
labelP1R.config(justify="center", bg="gray5", fg="snow")

labelP1R = Label(editor, text="R3 P4:", font=(24))
labelP1R.grid(row=6, column=9)
labelP1R.config(justify="center", bg="gray5", fg="snow")

labelP1R = Label(editor, text="R4 P4:", font=(24))
labelP1R.grid(row=7, column=9)
labelP1R.config(justify="center", bg="gray5", fg="snow")


#Botones de Edición

"""
En las variables pongo "P" como Posición del botón
mientras que en las filas significa Partitura
"C" significa lo mismo, Compás, partutura xd
"""

#C1

#R1
R1P1C1=Button(editor, command=boton_R1P1C1, text="   ")
R1P1C1.grid(row=0, column=1)
R1P1C1.config(bg="gray7", fg="snow")

R1P2C1=Button(editor, command=boton_R1P2C1, text="   ")
R1P2C1.grid(row=0, column=2)
R1P2C1.config(bg="gray7", fg="snow")

R1P3C1=Button(editor, command=boton_R1P3C1, text="   ")
R1P3C1.grid(row=0, column=3)
R1P3C1.config(bg="gray7", fg="snow")

R1P4C1=Button(editor, command=boton_R1P4C1, text="   ")
R1P4C1.grid(row=0, column=4)
R1P4C1.config(bg="gray7", fg="snow")

R1P5C1=Button(editor, command=boton_R1P5C1, text="   ")
R1P5C1.grid(row=0, column=5)
R1P5C1.config(bg="gray7", fg="snow")

R1P6C1=Button(editor, command=boton_R1P6C1, text="   ")
R1P6C1.grid(row=0, column=6)
R1P6C1.config(bg="gray7", fg="snow")

R1P7C1=Button(editor, command=boton_R1P7C1, text="   ")
R1P7C1.grid(row=0, column=7)
R1P7C1.config(bg="gray7", fg="snow")

R1P8C1=Button(editor, command=boton_R1P8C1, text="   ")
R1P8C1.grid(row=0, column=8)
R1P8C1.config(bg="gray7", fg="snow")

#R2
R2P1C1=Button(editor, command=boton_R2P1C1, text="   ")
R2P1C1.grid(row=1, column=1)
R2P1C1.config(bg="gray7", fg="snow")

R2P2C1=Button(editor, command=boton_R2P2C1, text="   ")
R2P2C1.grid(row=1, column=2)
R2P2C1.config(bg="gray7", fg="snow")

R2P3C1=Button(editor, command=boton_R2P3C1, text="   ")
R2P3C1.grid(row=1, column=3)
R2P3C1.config(bg="gray7", fg="snow")

R2P4C1=Button(editor, command=boton_R2P4C1, text="   ")
R2P4C1.grid(row=1, column=4)
R2P4C1.config(bg="gray7", fg="snow")

R2P5C1=Button(editor, command=boton_R2P5C1, text="   ")
R2P5C1.grid(row=1, column=5)
R2P5C1.config(bg="gray7", fg="snow")

R2P6C1=Button(editor, command=boton_R2P6C1, text="   ")
R2P6C1.grid(row=1, column=6)
R2P6C1.config(bg="gray7", fg="snow")

R2P7C1=Button(editor, command=boton_R2P7C1, text="   ")
R2P7C1.grid(row=1, column=7)
R2P7C1.config(bg="gray7", fg="snow")

R2P8C1=Button(editor, command=boton_R2P8C1, text="   ")
R2P8C1.grid(row=1, column=8)
R2P8C1.config(bg="gray7", fg="snow")

#R3
R3P1C1=Button(editor, command=boton_R3P1C1, text="   ")
R3P1C1.grid(row=2, column=1)
R3P1C1.config(bg="gray7", fg="snow")

R3P2C1=Button(editor, command=boton_R3P2C1, text="   ")
R3P2C1.grid(row=2, column=2)
R3P2C1.config(bg="gray7", fg="snow")

R3P3C1=Button(editor, command=boton_R3P3C1, text="   ")
R3P3C1.grid(row=2, column=3)
R3P3C1.config(bg="gray7", fg="snow")

R3P4C1=Button(editor, command=boton_R3P4C1, text="   ")
R3P4C1.grid(row=2, column=4)
R3P4C1.config(bg="gray7", fg="snow")

R3P5C1=Button(editor, command=boton_R3P5C1, text="   ")
R3P5C1.grid(row=2, column=5)
R3P5C1.config(bg="gray7", fg="snow")

R3P6C1=Button(editor, command=boton_R3P6C1, text="   ")
R3P6C1.grid(row=2, column=6)
R3P6C1.config(bg="gray7", fg="snow")

R3P7C1=Button(editor, command=boton_R3P7C1, text="   ")
R3P7C1.grid(row=2, column=7)
R3P7C1.config(bg="gray7", fg="snow")

R3P8C1=Button(editor, command=boton_R3P8C1, text="   ")
R3P8C1.grid(row=2, column=8)
R3P8C1.config(bg="gray7", fg="snow")

#R4
R4P1C1=Button(editor, command=boton_R4P1C1, text="   ")
R4P1C1.grid(row=3, column=1)
R4P1C1.config(bg="gray7", fg="snow")

R4P2C1=Button(editor, command=boton_R4P2C1, text="   ")
R4P2C1.grid(row=3, column=2)
R4P2C1.config(bg="gray7", fg="snow")

R4P3C1=Button(editor, command=boton_R4P3C1, text="   ")
R4P3C1.grid(row=3, column=3)
R4P3C1.config(bg="gray7", fg="snow")

R4P4C1=Button(editor, command=boton_R4P4C1, text="   ")
R4P4C1.grid(row=3, column=4)
R4P4C1.config(bg="gray7", fg="snow")

R4P5C1=Button(editor, command=boton_R4P5C1, text="   ")
R4P5C1.grid(row=3, column=5)
R4P5C1.config(bg="gray7", fg="snow")

R4P6C1=Button(editor, command=boton_R4P6C1, text="   ")
R4P6C1.grid(row=3, column=6)
R4P6C1.config(bg="gray7", fg="snow")

R4P7C1=Button(editor, command=boton_R4P7C1, text="   ")
R4P7C1.grid(row=3, column=7)
R4P7C1.config(bg="gray7", fg="snow")

R4P8C1=Button(editor, command=boton_R4P8C1, text="   ")
R4P8C1.grid(row=3, column=8)
R4P8C1.config(bg="gray7", fg="snow")

#C2

#R1
R1P1C2=Button(editor, command=boton_R1P1C2, text="   ")
R1P1C2.grid(row=0, column=10)
R1P1C2.config(bg="gray7", fg="snow")

R1P2C2=Button(editor, command=boton_R1P2C2, text="   ")
R1P2C2.grid(row=0, column=11)
R1P2C2.config(bg="gray7", fg="snow")

R1P3C2=Button(editor, command=boton_R1P3C2, text="   ")
R1P3C2.grid(row=0, column=12)
R1P3C2.config(bg="gray7", fg="snow")

R1P4C2=Button(editor, command=boton_R1P4C2, text="   ")
R1P4C2.grid(row=0, column=13)
R1P4C2.config(bg="gray7", fg="snow")

R1P5C2=Button(editor, command=boton_R1P5C2, text="   ")
R1P5C2.grid(row=0, column=14)
R1P5C2.config(bg="gray7", fg="snow")

R1P6C2=Button(editor, command=boton_R1P6C2, text="   ")
R1P6C2.grid(row=0, column=15)
R1P6C2.config(bg="gray7", fg="snow")

R1P7C2=Button(editor, command=boton_R1P7C2, text="   ")
R1P7C2.grid(row=0, column=16)
R1P7C2.config(bg="gray7", fg="snow")

R1P8C2=Button(editor, command=boton_R1P8C2, text="   ")
R1P8C2.grid(row=0, column=17)
R1P8C2.config(bg="gray7", fg="snow")

#R2
R2P1C2=Button(editor, command=boton_R2P1C2, text="   ")
R2P1C2.grid(row=1, column=10)
R2P1C2.config(bg="gray7", fg="snow")

R2P2C2=Button(editor, command=boton_R2P2C2, text="   ")
R2P2C2.grid(row=1, column=11)
R2P2C2.config(bg="gray7", fg="snow")

R2P3C2=Button(editor, command=boton_R2P3C2, text="   ")
R2P3C2.grid(row=1, column=12)
R2P3C2.config(bg="gray7", fg="snow")

R2P4C2=Button(editor, command=boton_R2P4C2, text="   ")
R2P4C2.grid(row=1, column=13)
R2P4C2.config(bg="gray7", fg="snow")

R2P5C2=Button(editor, command=boton_R2P5C2, text="   ")
R2P5C2.grid(row=1, column=14)
R2P5C2.config(bg="gray7", fg="snow")

R2P6C2=Button(editor, command=boton_R2P6C2, text="   ")
R2P6C2.grid(row=1, column=15)
R2P6C2.config(bg="gray7", fg="snow")

R2P7C2=Button(editor, command=boton_R2P7C2, text="   ")
R2P7C2.grid(row=1, column=16)
R2P7C2.config(bg="gray7", fg="snow")

R2P8C2=Button(editor, command=boton_R2P8C2, text="   ")
R2P8C2.grid(row=1, column=17)
R2P8C2.config(bg="gray7", fg="snow")

#R3
R3P1C2=Button(editor, command=boton_R3P1C2, text="   ")
R3P1C2.grid(row=2, column=10)
R3P1C2.config(bg="gray7", fg="snow")

R3P2C2=Button(editor, command=boton_R3P2C2, text="   ")
R3P2C2.grid(row=2, column=11)
R3P2C2.config(bg="gray7", fg="snow")

R3P3C2=Button(editor, command=boton_R3P3C2, text="   ")
R3P3C2.grid(row=2, column=12)
R3P3C2.config(bg="gray7", fg="snow")

R3P4C2=Button(editor, command=boton_R3P4C2, text="   ")
R3P4C2.grid(row=2, column=13)
R3P4C2.config(bg="gray7", fg="snow")

R3P5C2=Button(editor, command=boton_R3P5C2, text="   ")
R3P5C2.grid(row=2, column=14)
R3P5C2.config(bg="gray7", fg="snow")

R3P6C2=Button(editor, command=boton_R3P6C2, text="   ")
R3P6C2.grid(row=2, column=15)
R3P6C2.config(bg="gray7", fg="snow")

R3P7C2=Button(editor, command=boton_R3P7C2, text="   ")
R3P7C2.grid(row=2, column=16)
R3P7C2.config(bg="gray7", fg="snow")

R3P8C2=Button(editor, command=boton_R3P8C2, text="   ")
R3P8C2.grid(row=2, column=17)
R3P8C2.config(bg="gray7", fg="snow")

#R4
R4P1C2=Button(editor, command=boton_R4P1C2, text="   ")
R4P1C2.grid(row=3, column=10)
R4P1C2.config(bg="gray7", fg="snow")

R4P2C2=Button(editor, command=boton_R4P2C2, text="   ")
R4P2C2.grid(row=3, column=11)
R4P2C2.config(bg="gray7", fg="snow")

R4P3C2=Button(editor, command=boton_R4P3C2, text="   ")
R4P3C2.grid(row=3, column=12)
R4P3C2.config(bg="gray7", fg="snow")

R4P4C2=Button(editor, command=boton_R4P4C2, text="   ")
R4P4C2.grid(row=3, column=13)
R4P4C2.config(bg="gray7", fg="snow")

R4P5C2=Button(editor, command=boton_R4P5C2, text="   ")
R4P5C2.grid(row=3, column=14)
R4P5C2.config(bg="gray7", fg="snow")

R4P6C2=Button(editor, command=boton_R4P6C2, text="   ")
R4P6C2.grid(row=3, column=15)
R4P6C2.config(bg="gray7", fg="snow")

R4P7C2=Button(editor, command=boton_R4P7C2, text="   ")
R4P7C2.grid(row=3, column=16)
R4P7C2.config(bg="gray7", fg="snow")

R4P8C2=Button(editor, command=boton_R4P8C2, text="   ")
R4P8C2.grid(row=3, column=17)
R4P8C2.config(bg="gray7", fg="snow")

#C3

#R1
R1P1C3=Button(editor, command=boton_R1P1C3, text="   ")
R1P1C3.grid(row=4, column=1)
R1P1C3.config(bg="gray7", fg="snow")

R1P2C3=Button(editor, command=boton_R1P2C3, text="   ")
R1P2C3.grid(row=4, column=2)
R1P2C3.config(bg="gray7", fg="snow")

R1P3C3=Button(editor, command=boton_R1P3C3, text="   ")
R1P3C3.grid(row=4, column=3)
R1P3C3.config(bg="gray7", fg="snow")

R1P4C3=Button(editor, command=boton_R1P4C3, text="   ")
R1P4C3.grid(row=4, column=4)
R1P4C3.config(bg="gray7", fg="snow")

R1P5C3=Button(editor, command=boton_R1P5C3, text="   ")
R1P5C3.grid(row=4, column=5)
R1P5C3.config(bg="gray7", fg="snow")

R1P6C3=Button(editor, command=boton_R1P6C3, text="   ")
R1P6C3.grid(row=4, column=6)
R1P6C3.config(bg="gray7", fg="snow")

R1P7C3=Button(editor, command=boton_R1P7C3, text="   ")
R1P7C3.grid(row=4, column=7)
R1P7C3.config(bg="gray7", fg="snow")

R1P8C3=Button(editor, command=boton_R1P8C3, text="   ")
R1P8C3.grid(row=4, column=8)
R1P8C3.config(bg="gray7", fg="snow")

#R2
R2P1C3=Button(editor, command=boton_R2P1C3, text="   ")
R2P1C3.grid(row=5, column=1)
R2P1C3.config(bg="gray7", fg="snow")

R2P2C3=Button(editor, command=boton_R2P2C3, text="   ")
R2P2C3.grid(row=5, column=2)
R2P2C3.config(bg="gray7", fg="snow")

R2P3C3=Button(editor, command=boton_R2P3C3, text="   ")
R2P3C3.grid(row=5, column=3)
R2P3C3.config(bg="gray7", fg="snow")

R2P4C3=Button(editor, command=boton_R2P4C3, text="   ")
R2P4C3.grid(row=5, column=4)
R2P4C3.config(bg="gray7", fg="snow")

R2P5C3=Button(editor, command=boton_R2P5C3, text="   ")
R2P5C3.grid(row=5, column=5)
R2P5C3.config(bg="gray7", fg="snow")

R2P6C3=Button(editor, command=boton_R2P6C3, text="   ")
R2P6C3.grid(row=5, column=6)
R2P6C3.config(bg="gray7", fg="snow")

R2P7C3=Button(editor, command=boton_R2P7C3, text="   ")
R2P7C3.grid(row=5, column=7)
R2P7C3.config(bg="gray7", fg="snow")

R2P8C3=Button(editor, command=boton_R2P8C3, text="   ")
R2P8C3.grid(row=5, column=8)
R2P8C3.config(bg="gray7", fg="snow")

#R3
R3P1C3=Button(editor, command=boton_R3P1C3, text="   ")
R3P1C3.grid(row=6, column=1)
R3P1C3.config(bg="gray7", fg="snow")

R3P2C3=Button(editor, command=boton_R3P2C3, text="   ")
R3P2C3.grid(row=6, column=2)
R3P2C3.config(bg="gray7", fg="snow")

R3P3C3=Button(editor, command=boton_R3P3C3, text="   ")
R3P3C3.grid(row=6, column=3)
R3P3C3.config(bg="gray7", fg="snow")

R3P4C3=Button(editor, command=boton_R3P4C3, text="   ")
R3P4C3.grid(row=6, column=4)
R3P4C3.config(bg="gray7", fg="snow")

R3P5C3=Button(editor, command=boton_R3P5C3, text="   ")
R3P5C3.grid(row=6, column=5)
R3P5C3.config(bg="gray7", fg="snow")

R3P6C3=Button(editor, command=boton_R3P6C3, text="   ")
R3P6C3.grid(row=6, column=6)
R3P6C3.config(bg="gray7", fg="snow")

R3P7C3=Button(editor, command=boton_R3P7C3, text="   ")
R3P7C3.grid(row=6, column=7)
R3P7C3.config(bg="gray7", fg="snow")

R3P8C3=Button(editor, command=boton_R3P8C3, text="   ")
R3P8C3.grid(row=6, column=8)
R3P8C3.config(bg="gray7", fg="snow")

#R4
R4P1C3=Button(editor, command=boton_R4P1C3, text="   ")
R4P1C3.grid(row=7, column=1)
R4P1C3.config(bg="gray7", fg="snow")

R4P2C3=Button(editor, command=boton_R4P2C3, text="   ")
R4P2C3.grid(row=7, column=2)
R4P2C3.config(bg="gray7", fg="snow")

R4P3C3=Button(editor, command=boton_R4P3C3, text="   ")
R4P3C3.grid(row=7, column=3)
R4P3C3.config(bg="gray7", fg="snow")

R4P4C3=Button(editor, command=boton_R4P4C3, text="   ")
R4P4C3.grid(row=7, column=4)
R4P4C3.config(bg="gray7", fg="snow")

R4P5C3=Button(editor, command=boton_R4P5C3, text="   ")
R4P5C3.grid(row=7, column=5)
R4P5C3.config(bg="gray7", fg="snow")

R4P6C3=Button(editor, command=boton_R4P6C3, text="   ")
R4P6C3.grid(row=7, column=6)
R4P6C3.config(bg="gray7", fg="snow")

R4P7C3=Button(editor, command=boton_R4P7C3, text="   ")
R4P7C3.grid(row=7, column=7)
R4P7C3.config(bg="gray7", fg="snow")

R4P8C3=Button(editor, command=boton_R4P8C3, text="   ")
R4P8C3.grid(row=7, column=8)
R4P8C3.config(bg="gray7", fg="snow")

#C4

#R1
R1P1C4=Button(editor, command=boton_R1P1C4, text="   ")
R1P1C4.grid(row=4, column=10)
R1P1C4.config(bg="gray7", fg="snow")

R1P2C4=Button(editor, command=boton_R1P2C4, text="   ")
R1P2C4.grid(row=4, column=11)
R1P2C4.config(bg="gray7", fg="snow")

R1P3C4=Button(editor, command=boton_R1P3C4, text="   ")
R1P3C4.grid(row=4, column=12)
R1P3C4.config(bg="gray7", fg="snow")

R1P4C4=Button(editor, command=boton_R1P4C4, text="   ")
R1P4C4.grid(row=4, column=13)
R1P4C4.config(bg="gray7", fg="snow")

R1P5C4=Button(editor, command=boton_R1P5C4, text="   ")
R1P5C4.grid(row=4, column=14)
R1P5C4.config(bg="gray7", fg="snow")

R1P6C4=Button(editor, command=boton_R1P6C4, text="   ")
R1P6C4.grid(row=4, column=15)
R1P6C4.config(bg="gray7", fg="snow")

R1P7C4=Button(editor, command=boton_R1P7C4, text="   ")
R1P7C4.grid(row=4, column=16)
R1P7C4.config(bg="gray7", fg="snow")

R1P8C4=Button(editor, command=boton_R1P8C4, text="   ")
R1P8C4.grid(row=4, column=17)
R1P8C4.config(bg="gray7", fg="snow")

#R2
R2P1C4=Button(editor, command=boton_R2P1C4, text="   ")
R2P1C4.grid(row=5, column=10)
R2P1C4.config(bg="gray7", fg="snow")

R2P2C4=Button(editor, command=boton_R2P2C4, text="   ")
R2P2C4.grid(row=5, column=11)
R2P2C4.config(bg="gray7", fg="snow")

R2P3C4=Button(editor, command=boton_R2P3C4, text="   ")
R2P3C4.grid(row=5, column=12)
R2P3C4.config(bg="gray7", fg="snow")

R2P4C4=Button(editor, command=boton_R2P4C4, text="   ")
R2P4C4.grid(row=5, column=13)
R2P4C4.config(bg="gray7", fg="snow")

R2P5C4=Button(editor, command=boton_R2P5C4, text="   ")
R2P5C4.grid(row=5, column=14)
R2P5C4.config(bg="gray7", fg="snow")

R2P6C4=Button(editor, command=boton_R2P6C4, text="   ")
R2P6C4.grid(row=5, column=15)
R2P6C4.config(bg="gray7", fg="snow")

R2P7C4=Button(editor, command=boton_R2P7C4, text="   ")
R2P7C4.grid(row=5, column=16)
R2P7C4.config(bg="gray7", fg="snow")

R2P8C4=Button(editor, command=boton_R2P8C4, text="   ")
R2P8C4.grid(row=5, column=17)
R2P8C4.config(bg="gray7", fg="snow")

#R3
R3P1C4=Button(editor, command=boton_R3P1C4, text="   ")
R3P1C4.grid(row=6, column=10)
R3P1C4.config(bg="gray7", fg="snow")

R3P2C4=Button(editor, command=boton_R3P2C4, text="   ")
R3P2C4.grid(row=6, column=11)
R3P2C4.config(bg="gray7", fg="snow")

R3P3C4=Button(editor, command=boton_R3P3C4, text="   ")
R3P3C4.grid(row=6, column=12)
R3P3C4.config(bg="gray7", fg="snow")

R3P4C4=Button(editor, command=boton_R3P4C4, text="   ")
R3P4C4.grid(row=6, column=13)
R3P4C4.config(bg="gray7", fg="snow")

R3P5C4=Button(editor, command=boton_R3P5C4, text="   ")
R3P5C4.grid(row=6, column=14)
R3P5C4.config(bg="gray7", fg="snow")

R3P6C4=Button(editor, command=boton_R3P6C4, text="   ")
R3P6C4.grid(row=6, column=15)
R3P6C4.config(bg="gray7", fg="snow")

R3P7C4=Button(editor, command=boton_R3P7C4, text="   ")
R3P7C4.grid(row=6, column=16)
R3P7C4.config(bg="gray7", fg="snow")

R3P8C4=Button(editor, command=boton_R3P8C4, text="   ")
R3P8C4.grid(row=6, column=17)
R3P8C4.config(bg="gray7", fg="snow")

#R4
R4P1C4=Button(editor, command=boton_R4P1C4, text="   ")
R4P1C4.grid(row=7, column=10)
R4P1C4.config(bg="gray7", fg="snow")

R4P2C4=Button(editor, command=boton_R4P2C4, text="   ")
R4P2C4.grid(row=7, column=11)
R4P2C4.config(bg="gray7", fg="snow")

R4P3C4=Button(editor, command=boton_R4P3C4, text="   ")
R4P3C4.grid(row=7, column=12)
R4P3C4.config(bg="gray7", fg="snow")

R4P4C4=Button(editor, command=boton_R4P4C4, text="   ")
R4P4C4.grid(row=7, column=13)
R4P4C4.config(bg="gray7", fg="snow")

R4P5C4=Button(editor, command=boton_R4P5C4, text="   ")
R4P5C4.grid(row=7, column=14)
R4P5C4.config(bg="gray7", fg="snow")

R4P6C4=Button(editor, command=boton_R4P6C4, text="   ")
R4P6C4.grid(row=7, column=15)
R4P6C4.config(bg="gray7", fg="snow")

R4P7C4=Button(editor, command=boton_R4P7C4, text="   ")
R4P7C4.grid(row=7, column=16)
R4P7C4.config(bg="gray7", fg="snow")

R4P8C4=Button(editor, command=boton_R4P8C4, text="   ")
R4P8C4.grid(row=7, column=17)
R4P8C4.config(bg="gray7", fg="snow")


#Atajos de teclado

raiz.bind("M", tempo_manual)
raiz.bind("m", tempo_manual)

def play_pause(event):
    if activador:
        Pausar()
    else:
        Play()

raiz.bind("P", play_pause)
raiz.bind("p", play_pause)


#lista para acceder a las variables de botones de editor de forma más eficiente uwu!
numero_boton = [R1P1C1, R1P2C1, R1P3C1, R1P4C1, R1P5C1, R1P6C1, R1P7C1, R1P8C1, R2P1C1, R2P2C1, R2P3C1, R2P4C1, R2P5C1, R2P6C1,
R2P7C1, R2P8C1, R3P1C1, R3P2C1, R3P3C1, R3P4C1, R3P5C1, R3P6C1, R3P7C1, R3P8C1, R4P1C1, R4P2C1, R4P3C1, R4P4C1, R4P5C1, R4P6C1,
R4P7C1, R4P8C1, R1P1C2, R1P2C2, R1P3C2, R1P4C2, R1P5C2, R1P6C2, R1P7C2, R1P8C2, R2P1C2, R2P2C2, R2P3C2, R2P4C2, R2P5C2, R2P6C2,
R2P7C2, R2P8C2, R3P1C2, R3P2C2, R3P3C2, R3P4C2, R3P5C2, R3P6C2, R3P7C2, R3P8C2, R4P1C2, R4P2C2, R4P3C2, R4P4C2, R4P5C2, R4P6C2,
R4P7C2, R4P8C2, R1P1C3, R1P2C3, R1P3C3, R1P4C3, R1P5C3, R1P6C3, R1P7C3, R1P8C3, R2P1C3, R2P2C3, R2P3C3, R2P4C3, R2P5C3, R2P6C3,
R2P7C3, R2P8C3, R3P1C3, R3P2C3, R3P3C3, R3P4C3, R3P5C3, R3P6C3, R3P7C3, R3P8C3, R4P1C3, R4P2C3, R4P3C3, R4P4C3, R4P5C3, R4P6C3,
R4P7C3, R4P8C3, R1P1C4, R1P2C4, R1P3C4, R1P4C4, R1P5C4, R1P6C4, R1P7C4, R1P8C4, R2P1C4, R2P2C4, R2P3C4, R2P4C4, R2P5C4, R2P6C4,
R2P7C4, R2P8C4, R3P1C4, R3P2C4, R3P3C4, R3P4C4, R3P5C4, R3P6C4, R3P7C4, R3P8C4, R4P1C4, R4P2C4, R4P3C4, R4P4C4, R4P5C4, R4P6C4,
R4P7C4, R4P8C4]


inicio.play()

raiz.mainloop()
activador = False

time.sleep(.5)
final.play()
time.sleep(3)
