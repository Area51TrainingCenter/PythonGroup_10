# pip install dlib face_recognition
import argparse

import face_recognition
from PIL import Image, ImageDraw


def poner_bigote(imagen_entrada):
    bigote = Image.open('bigote.png')
    nombre_archivo = imagen_entrada.filename
    imagen = face_recognition.load_image_file(nombre_archivo)
    landmarks = face_recognition.face_landmarks(imagen)
    nariz_x, nariz_y = landmarks[0]['nose_tip'][2]

    imagen_salida = imagen_entrada.copy()
    bigote.thumbnail((60, 60,))
    imagen_salida.paste(bigote, (nariz_x - int(bigote.size[0]/2), nariz_y), bigote)
    return imagen_salida


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='superman.py')
    parser.add_argument('input', type=str, help='Imagen de entrada')
    parser.add_argument('output', nargs='?', type=str, help='Imagen de salida')
    arguments = parser.parse_args()
    imagen_entrada = Image.open(arguments.input)
    imagen_salida = poner_bigote(imagen_entrada)
    imagen_salida.save(
        arguments.output or arguments.input.replace('.', '_bigote.')
    )
