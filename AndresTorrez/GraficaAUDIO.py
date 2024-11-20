import librosa
import librosa.display
import matplotlib.pyplot as plt

class Analizadoraudio:
    def _init_(self, ruta_audio):
        self.ruta_audio = ruta_audio
        self.audio, self.tasa_muestreo = librosa.load(ruta_audio)

    def graficar(self):
        plt.figure(figsize=(10, 4))
        librosa.display.waveshow(self.audio, sr=self.tasa_muestreo)
        plt.title("Forma de onda del audio")
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Amplitud")
        plt.savefig("Grafica.png")
        print("Grafica guardada como 'Grafica.png'")

    def duracion_audio(self):
        return librosa.get_duration(y=self.audio, sr=self.tasa_muestreo)


analizador = Analizadoraudio("/audio1.mp3")
print(f"Duración del audio: {analizador.duracion_audio()} segundos")
analizador.graficar()