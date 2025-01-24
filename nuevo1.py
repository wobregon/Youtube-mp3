import tkinter as tk
from tkinter import messagebox, filedialog
from pytube import YouTube
from pydub import AudioSegment
import os

def download_mp3():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Por favor, ingresa una URL válida de YouTube.")
        return

    # Seleccionar directorio de descarga
    save_path = filedialog.askdirectory()
    if not save_path:
        return

    try:
        # Descargar video desde YouTube
        yt = YouTube(url)
        video_stream = yt.streams.filter(only_audio=True).first()
        if not video_stream:
            messagebox.showerror("Error", "No se pudo encontrar un flujo de audio.")
            return

        # Descargar el archivo de audio
        downloaded_file = video_stream.download(output_path=save_path)

        # Convertir el archivo a MP3
        base, ext = os.path.splitext(downloaded_file)
        mp3_file = f"{base}.mp3"
        audio = AudioSegment.from_file(downloaded_file)
        audio.export(mp3_file, format="mp3")
        os.remove(downloaded_file)  # Eliminar archivo original (opcional)

        messagebox.showinfo("Éxito", f"El archivo MP3 se ha descargado correctamente en: {mp3_file}")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo descargar el archivo: {str(e)}")

# Crear interfaz gráfica
root = tk.Tk()
root.title("Descargador de MP3 desde YouTube")

# Etiqueta y campo para la URL
url_label = tk.Label(root, text="Ingresa la URL del video de YouTube:")
url_label.pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Botón para iniciar la descarga
download_button = tk.Button(root, text="Descargar MP3", command=download_mp3, bg="green", fg="white")
download_button.pack(pady=20)

# Ejecutar la aplicación
root.mainloop()
