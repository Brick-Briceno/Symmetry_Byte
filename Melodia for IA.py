import os
import glob
import random
import mido
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.models import Sequential
from tkinter import *
from tkinter import filedialog

# Función para cargar los archivos MIDI
def cargar_midi(path):
    mid = mido.MidiFile(path)
    return mid.play()

# Función para cargar los datos de entrenamiento
def cargar_datos(path):
    datos = []
    for archivo in glob.glob(path + '/*.mid'):
        mid = mido.MidiFile(archivo)
        notas = []
        for mensaje in mid.play():
            if mensaje.type == 'note_on':
                nota = mensaje.note
                tiempo = mensaje.time
                notas.append([nota, tiempo])
        datos.extend(notas)
    return datos

# Función para crear el modelo de red neuronal
def crear_modelo(longitud_secuencia, n_notas, n_units):
    modelo = Sequential()
    modelo.add(LSTM(n_units, input_shape=(longitud_secuencia, n_notas)))
    modelo.add(Dense(n_notas, activation='softmax'))
    modelo.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return modelo

# Función para generar una melodía utilizando la red neuronal
def generar_melodia(modelo, longitud_secuencia, n_notas, notas_iniciales, n_notas_generar):
    notas_generadas = list(notas_iniciales)
    notas_actuales = list(notas_iniciales)
    for i in range(n_notas_generar):
        entrada = np.zeros((1, longitud_secuencia, n_notas))
        for j, nota in enumerate(notas_actuales):
            entrada[0, j, nota] = 1
        probabilidad = modelo.predict(entrada)[0]
        probabilidad /= sum(probabilidad)
        siguiente_nota = np.random.choice(range(n_notas), p=probabilidad)
        notas_generadas.append(siguiente_nota)
        notas_actuales.append(siguiente_nota)
        notas_actuales.pop(0)
    return notas_generadas

# Función para reproducir una melodía utilizando una onda senoidal
def reproducir_melodia(notas, tempo, duracion_nota):
    for nota in notas:
        frecuencia = 440 * 2 ** ((nota - 69) / 12)
        duracion = duracion_nota * tempo
        onda = np.sin(2 * np.pi * np.arange(int(duracion * 44100)) * frecuencia / 44100)
        reproduccion = mido.Message('note_on', note=nota, velocity=127, time=0)
        reproduccion.time = int(duracion * 1000)
        reproduccion_off = mido.Message('note_off', note=nota, velocity=0, time=0)
        reproduccion_off.time = reproduccion.time
        port_out.send(reproduccion)
        stream.write(onda.astype(np.float32).tobytes())
        port_out.send(reproduccion_off)

