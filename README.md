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
Obteniendo así de las diferentes ventanas la Transformada de Fourier y el espcetro de frecuencias. 
![ventana_1](https://github.com/user-attachments/assets/566206fb-726d-49ed-9c77-01ec71fa05e5)
![ventana_2](https://github.com/user-attachments/assets/45228098-1ca5-429f-9694-853e108d3aef)
![ventana_3](https://github.com/user-attachments/assets/718379ff-009b-465e-88d2-9e62374ca18b)
![ventana_4](https://github.com/user-attachments/assets/42f1498f-c772-4a8c-98b9-b3f36cc901bc)
![ventana_5](https://github.com/user-attachments/assets/1dc59f42-fc4a-4183-a02a-f1eb975ce702)
![ventana_6](https://github.com/user-attachments/assets/007b349a-0003-44dc-ba64-1b4d721382ec)
![ventana_7](https://github.com/user-attachments/assets/9174ac4d-731b-4144-9061-ebf72bc4ac3b)
![ventana_8](https://github.com/user-attachments/assets/ca3038e4-b095-43a5-b203-502c66a30591)
![ventana_9](https://github.com/user-attachments/assets/bbbb28e0-2a04-4a66-9e1e-22e52ef06ce1)
![ventana_10](https://github.com/user-attachments/assets/e0d211a0-840b-47a1-ad3d-2444042dc688)












