import tkinter as tk
import numpy as np
import simpleaudio as sa
import mido

# Crea una matriz de botones para el piano roll
matrix = np.zeros((35, 64), dtype=int)

# Función para cambiar el estado del botón (de 0 a 1 o de 1 a 0)
def change_button_state(button):
    if matrix[button.grid_info()["row"]-2, button.grid_info()["column"]] == 0:
        matrix[button.grid_info()["row"]-2, button.grid_info()["column"]] = 1
        button.config(bg="#591F1D")
    else:
        matrix[button.grid_info()["row"]-2, button.grid_info()["column"]] = 0
        button.config(bg="white")

# Función para reproducir la melodía generada
def play_melody(melody, bpm):
    note_duration = 60 / bpm / 4
    midi_file = mido.MidiFile()
    track = mido.MidiTrack()
    midi_file.tracks.append(track)
    velocity = 64

    for i in range(melody.shape[0]):
        for j in range(melody.shape[1]):
            if melody[i, j] == 1:
                note = 48 + i + j*7
                note_on = mido.Message('note_on', note=note, velocity=velocity, time=int(note_duration * 1000))
                note_off = mido.Message('note_off', note=note, velocity=velocity, time=int(note_duration * 1000))
                track.append(note_on)
                track.append(note_off)

    with open("melody.mid", 'wb') as file:
        midi_file.save(file)

    wave = np.zeros((int(bpm * melody.shape[1] * 60 / 4), 1))
    time = 0

    for i in range(melody.shape[1]):
        for j in range(melody.shape[0]):
            if melody[j, i] == 1:
                frequency = 440 * 2 ** ((j+3) / 12)
                duration = note_duration * 4
                t = np.linspace(time, time + duration, int(duration * bpm))
                wave[int(time * bpm):int((time + duration) * bpm)] += np.sin(2 * np.pi * frequency * t) * 0.1
        time += note_duration * 4

    # Reproduce la melodía generada
    play_obj = sa.play_buffer((wave * (2**15 - 1)).astype(np.int16), 1, 2, bpm)
    play_obj.wait_done()

# Función para reproducir la melodía generada
def play():
    bpm = 120 # Establece el tempo a 120 BPM
    play_melody(matrix, bpm)

# Función para pausar la reproducción de la melodía
def pause():
    play_obj.stop()

# Crea la ventana principal
root = tk.Tk()

# Crea los botones para el piano roll
buttons = []
for i in range(35):
    for j in range(64):
        button = tk.Button(root, width=2, height=1, bg="white", command=lambda b=button: change_button_state(b))
        button.grid(row=i+2, column=j)
        buttons.append(button)

# Agrega
