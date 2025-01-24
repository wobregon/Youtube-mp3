Instala las bibliotecas necesarias: Ejecuta el siguiente comando para instalar las dependencias:

pip install pytube pydub

También asegúrate de tener instalado ffmpeg, que es necesario para la conversión de audio:

Windows: Descarga y configura ffmpeg y agrega su ruta a las variables de entorno.
Linux/MacOS: Instálalo con tu gestor de paquetes:

sudo apt install ffmpeg  # Linux
brew install ffmpeg      # macOS


Ejecuta el script.
Ingresa la URL de un video de YouTube.
Selecciona una carpeta donde guardar el archivo MP3.
Presiona el botón "Descargar MP3".

Si pytube falla por cambios en la API de YouTube, actualiza la biblioteca:
pip install --upgrade pytube

CONSIDERACIONES: Asegúrate de respetar los derechos de autor y utilizar el programa únicamente para contenido que tengas permitido descargar.
