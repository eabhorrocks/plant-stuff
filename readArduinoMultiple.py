import serial
import numpy
import matplotlib
import matplotlib.pyplot as plt
from drawnow import *

arduinoData = serial.Serial("/dev/ttyACM0", 9600)
moistureVals = [];
humidityVals = [];
tempVals = [];
plt.ion() #interactive mode to plot live data
cnt = 0

def plotData(): ##makeFig():
    plt.subplot(2,2,1)
    plt.ylim(0,800)
    plt.title('Moisture levels')
    plt.grid(True)
    plt.ylabel('Moisture a/u')
    plt.plot(moistureVals, 'b-o')
    plt.subplot(2,2,3)
    plt.ylim(0,30)
    plt.title('Temperature')
    plt.grid(True)
    plt.ylabel('Celcius')
    plt.plot(tempVals, 'r-o')
    plt.subplot(2,2,2)
    plt.ylim(0,100)
    plt.title('Humidity levels')
    plt.grid(True)
    plt.ylabel('%')
    plt.plot(humidityVals, 'g-o')
    plt.show


while True:
    while (arduinoData.inWaiting() == 0):
        pass
    arduinoString = arduinoData.readline().strip()
    data = arduinoString.decode('utf-8')
    
    if(data[0]=="m"): ## moisture levels reading
        newMoistVal = data.replace('m','') ## gets rid of the m tag
        moisture = float(newMoistVal)
        moistureVals.append(moisture)
        drawnow(plotData)
        plt.pause(.1)
        cnt = cnt+1
        if(cnt>50):
            moistureVals.pop(0)
            
    if(data[0]=="h"): ## humidity reading
        newHumVal = data.replace('h','') ## gets rid of tag
        humidity = float(newHumVal)
        humidityVals.append(humidity)
        drawnow(plotData)
        plt.pause(.1)
        cnt = cnt+1
        if(cnt>50):
            humidityVals.pop(0)
            
    if(data[0]=="t"): ## temperature reading
        newTempVal = data.replace('t','') ## gets rid of the m tag
        temperature = float(newTempVal)
        tempVals.append(temperature)
        drawnow(plotData)
        plt.pause(.1)
        cnt = cnt+1
        if(cnt>50):
            tempVals.pop(0)

