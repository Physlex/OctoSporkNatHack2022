import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from scipy import signal

class CSV:
    def __init__(self, file) -> None:
        self.data_frame = pd.read_csv(file, delimiter=",")
        self.timestamps_channel = self.data_frame["timestamps"]
        self.TP9 = self.data_frame["TP9"]
        self.AF7 = self.data_frame["AF7"]
        self.AF8 = self.data_frame["AF8"]
        self.TP10 = self.data_frame["TP10"]
        self.RightAUX = self.data_frame["Right AUX"]
        pass

    def get_data(self):
        return self.data_frame

    def get_timestamps(self):
        return self.timestamps_channel

    def get_AF7(self):
        return self.AF7

    def get_AF8(self):
        return self.AF8

    def get_TP9(self):
        return self.TP9

    def get_TP10(self):
        return self.TP10
        
    def get_RightAUX(self):
        return self.RightAUX

class ChannelPlot:
    def __init__(self, file) -> None:
        pass

    def link_to_plot(self, file):
        # Create variables and link to plot
        csv = CSV(file)
        self.channel = csv.get_TP9()
        time = np.arange(0, len(self.channel), 1)
        plt.plot(time, self.channel)
        pass

    def create_axis(self, x_label, y_label):
        # Create labels, with titles
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        pass

    def show_plot(self):
        # Display
        plt.show()
        self.__clean()
        pass

    def __clean(self): # This is 'Private' and cannot be called outside of this class
        # Cleanup?
        plt.clf()
        pass

class Fourier:
    def __init__(self, channel) -> None:
        self.channel = channel
        pass

    def link_to_plot(self, file):
        #define variables
        csv = CSV(file)
        self.channel = csv.get_AF8()
        pass

    def FFT(self):
        # Fourier transform
        self.fftData = np.fft.fft(self.channel)
        self.freq = np.fft.fftfreq(len(self.channel))*250
        self.fftData = self.fftData[1:int(len(self.fftData)/2)] # Remove unnecessary negative reflection
        self.freq = self.freq[1:int(len(self.freq)/2)]
        self.fftData = np.sqrt(self.fftData.real**2 + self.fftData.imag**2) # Recall FFT is a complex function
        pass

    def create_plot(self):
        plt.plot(self.freq, self.fftData)
        pass

    def create_axis(self, x_label, y_label):
        # Create labels, with titles
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        pass

    def show_plot(self):
        # Display
        plt.show()
        self.__clean()
        pass

    def __clean(self): # This is 'Private' and cannot be called outside of this class
        # Cleanup?
        plt.clf()
        pass

class Bands:
    def __init__(self, bands) -> None:
        self.bands=bands
        pass

    def plot_bands(self):
        binNames = ["Alpha", "Beta"]
        plt.ylabel("Amplitude")
        plt.bar(binNames, self.bands, color="#7967e1")
        plt.show()
        plt.clf()
        pass

class Bin:
    def __init__(self, channel) -> None:
        self.freq = np.fft.fftfreq(len(channel))*250
        self.channel = channel
        self.bandTotals = [0,0]
        self.bandCounts = [0,0]
        pass

    def alpha_beta(self, fftData):
        for point in range(len(self.freq)):
            if (self.freq[point] >= 8) and (
                self.freq[point] <=11):
                self.bandTotals[0] += fftData[point]
                self.bandCounts[0] += 1

            if(self.freq[point] >= 12) and (
               self.freq[point] <=35):
                self.bandTotals[1] += fftData[point]
                self.bandCounts[1] += 1
        pass

    def bands(self):
        # Save the average of all points 
        bands = list(np.array(self.bandTotals)/np.array(self.bandCounts))
       
        new_bands = Bands(bands)
        new_bands.plot_bands()
            
class Builder:
    def __init__(self, file) -> None:
        self.file = file
        pass

    def create_channel_plot(self):
        self.channelplot = ChannelPlot(self.file)
        self.channelplot.link_to_plot(self.file)
        self.channelplot.create_axis("sample", "uV")
        self.channelplot.show_plot()
        pass

    def fourier(self):
        self.FFT = Fourier(self.channelplot.channel)
        self.FFT.link_to_plot(self.file)
        self.FFT.FFT()
        self.FFT.create_plot()
        self.FFT.create_axis("Frequency (Hz)", "Magnitude")
        self.FFT.show_plot()
        pass
    
    def create_Bin(self):
        self.Bin = Bin(self.channelplot.channel)
        self.Bin.alpha_beta(self.FFT.fftData)
        self.Bin.bands()
        pass 




if __name__ == "__main__":
    fml = Builder("EEG_demo.csv")
    fml.create_channel_plot()
    fml.fourier()
    fml.create_Bin()
    pass



