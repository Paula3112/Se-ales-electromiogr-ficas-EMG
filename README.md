# EMG
El electromiograma (EMG) es una grabación de la actividad eléctrica de los músculos, también llamada actividad mioeléctrica. Existen dos tipos de EMG, el de superficie y el intramuscular o de aguja. 
Para poder realizar la captura de las señales mioeléctricas se utilizan dos electrodos activos y un electrodo de tierra. En el caso de los electrodos desuperficie, deben ser ubicados en la piel sobre el músculo a estudiar, mientras que el electrodo de tierra se conecta a una parte del cuerpo eléctricamente activa. La señal EMG será la diferencia entre las señales medidas por los electrodos activos. 
Los rangos de frecuencia EMG pueden variar entre (FRECUENCIA)


## Preparación
Para la captura de la señal se preparo al sujeto, colocando los electrodos de superficie sobre el músculo largo palmar y músculo braquirradial como se logra ver en la imagen, colocando el electrodo de tierra sobre el epicondilio medio. 

![Imagen de WhatsApp 2025-03-26 a las 23 17 12_c328d094](https://github.com/user-attachments/assets/e993660d-20cb-40b9-b269-3993543d67d3)
*Imagen1. posicion de los electrodos*


Para la captura de la señal EMG se utilizó un modulo AD8232 previamente conectado a un sistema de adquisición de datos DAQ, la frecuencia de muestreo que utilizamos fue de 5000 Hz, obteniendo así la siguiente señal EMG.

![saraa](https://github.com/user-attachments/assets/e5db7a64-e507-445b-89e9-930e71df5a64)
*Imagen2. Señal obtenida*

## Filtrado de la señal
Se aplicaron dos tipos de filtros, un pasa altas para eliminar los componentes de baja frecuencia y un filtro pasa bajas para elimiinar frecuencias no deseadas, como en nuestro caso ruido ECG; con estos filtros logramos obtener una señal sin ruido como se observa en la imagen. 

![señal filtrada](https://github.com/user-attachments/assets/3067e563-bbf1-4fd3-9950-24c189059174)
*Imagen3. Señal filtrada*

Se obtuvo con el siguiente codigo:
```
def butter_highpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a
  ```  

## Aventanamiento 
Para el aventanamiento dividimos la señal usando la ventana Hanning (EXPLICACIÓN) obteniendo así estas ventanas de la señal. 
(IMAGENN VENTANAS EN LA SEÑAL)
Obteniendo así de las diferentes ventanas la Transformada de Fourier y el espcetro de frecuencias. 
(IMAGEN FFT Y ESPECTRO) 



