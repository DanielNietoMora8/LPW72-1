import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os

class Audio:
    """Clase para procesar archivos de audio utilizando librosa."""
    
    def __init__(self, ruta_audio):
        
        #Inicializa la clase con la ruta del archivo de audio.
        
        self.ruta_audio = ruta_audio
        self.y = None
        self.sr = None

    def cargar_audio(self):
        
        #Carga el audio desde la ruta proporcionada y guarda sus datos.
        
        
        self.y, self.sr = librosa.load(self.ruta_audio, sr=None)
        
        

    def extraer_waveform(self):
        
        #Retorna la forma de onda del audio como un array.
        
        
        self.cargar_audio()
        return self.y

    def graficar_waveform(self):
        
        #Genera una gráfica de la forma de onda del audio usando matplotlib.
        
        
        self.cargar_audio()

        plt.figure(figsize=(12, 4))
        librosa.display.waveshow(self.y, sr=self.sr, alpha=0.8)
        plt.title("Forma de Onda del Audio")
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Amplitud")
        plt.tight_layout()
        plt.show()

    def guardar_grafica_waveform(self, nombre_archivo="waveform.png"):
        
        #Guarda la gráfica de la forma de onda como un archivo PNG.
        
        
        self.cargar_audio()

        plt.figure(figsize=(12, 4))
        librosa.display.waveshow(self.y, sr=self.sr, alpha=0.8)
        plt.title("Forma de Onda del Audio")
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Amplitud")
        plt.tight_layout()

        # Guarda en la carpeta del script
        ruta_salida = os.path.join(os.getcwd(), nombre_archivo)
        plt.savefig(ruta_salida)
        plt.close()  # Cierra la figura 
        print(f"Gráfica guardada en: {ruta_salida}")

    

    

# Función principal
def main():
    # Ruta del archivo de audio 
    ruta_audio = "acoustic.mp3"

    # Crear instancia de AudioProcessor
    procesador = Audio(ruta_audio)

    # Extraer y mostrar la forma de onda en un array
    print("forma de onda...")
    waveform = procesador.extraer_waveform()
    print(f"Forma de onda extraída en array: {waveform[:8]} (primeros 8 valores)")

    # Graficar y guardar la forma de onda
    print("gráfica de la forma de onda...")
    procesador.graficar_waveform()
    procesador.guardar_grafica_waveform()

    


main()