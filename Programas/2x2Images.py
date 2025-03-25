from PIL import Image
import requests
from io import BytesIO

def convertir_a_2x2(input_url, output_path):
    tamaño = (600, 600)
    response = requests.get(input_url)
    imagen = Image.open(BytesIO(response.content))
    imagen = imagen.resize(tamaño, Image.LANCZOS)
    imagen.save(output_path)

convertir_a_2x2(
    "https://images.unsplash.com/photo-1614162692292-7ac56d7f7f1e?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8Zm9uZG8lMjBkZSUyMHBhbnRhbGxhJTIwcG9yc2NoZXxlbnwwfHwwfHx8MA%3D%3D", # Imagen a convertir
    "c:/Users/Jeremy Dominguez/Desktop/JeremyEmpre.jpg", # Donde se guardara la imagen
)
