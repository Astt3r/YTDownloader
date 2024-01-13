from pytube import YouTube
import os

def descargar_video(url, output_path):
    try:
        yt = YouTube(url)
        print(f"Descargando Video: {yt.title}...")
        yt.streams.get_highest_resolution().download(output_path=output_path)
        print(f"{yt.title} descargado exitosamente en {output_path}")
    except Exception as e:
        print(f"No se pudo descargar el video: {str(e)}")

def main():
    url = input("Introduce la URL del video de Youtube: ")

    # Obtener ruta de directorio de proyecto
    project_directory = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(project_directory, 'descargas')  # Directorio 'descargas' dentro del directorio del proyecto

    # Crear directorio de descargas si no existe
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    descargar_video(url, output_path)

if __name__ == "__main__":
    main()
