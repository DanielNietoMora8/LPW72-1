import librosa as lb
import matplotlib.pyplot as plt
import numpy as np

class Audio:
    def __init__(self, audio):
        self.audio = audio
        self.y, self.sr = lb.load(f"{audio}", sr=None)

    def waveFormArray(self):
        return self.y #Retorno Array de forma de onda
    
    def waveFormShow(self):
        plt.plot(self.y) #Grafico forma de onda
        audio1.saveWaveForm()
        plt.show()

    def saveWaveForm(self):
        plt.savefig("waveform.png")
    
    def espectograma(self):
        D = np.abs(lb.stft(self.y))

        lb.display.specshow(lb.amplitude_to_db(D), y_axis="linear", x_axis="time")
        plt.colorbar()
        plt.show()


audio1 = Audio("sample.wav")

print(audio1.waveFormArray())

audio1.waveFormShow()

audio1.espectograma()

