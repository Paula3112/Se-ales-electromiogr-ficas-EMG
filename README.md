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

![Figure_1](https://github.com/user-attachments/assets/351e1289-3d17-4f86-87eb-072f8036f45d)


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
![ven1](https://github.com/user-attachments/assets/85d03159-01f2-43b4-be49-1b1e84fafb20)
![ven2](https://github.com/user-attachments/assets/33270b59-e970-4f08-b1d4-7f60f15124ef)
![ven3](https://github.com/user-attachments/assets/32212ae9-b3a7-4080-926d-3addaeed6cf6)
![ven4](https://github.com/user-attachments/assets/61326f83-4fa6-4640-bca1-77916b2e65e6)
![ven5](https://github.com/user-attachments/assets/b6ae0656-9e93-4eac-bd48-87e069ff2264)
![ven6](https://github.com/user-attachments/assets/0eeb9dde-b7f0-49a1-bb97-0b134955389c)
![ven7](https://github.com/user-attachments/assets/55d71b29-38c4-4c02-a405-85cf69ad0ae9)
![ven8](https://github.com/user-attachments/assets/b400e04d-2cbd-400d-8d33-691d8cef756e)
![ven9](https://github.com/user-attachments/assets/c704fcc6-c607-4433-9ac2-6d3b06e99bbd)
![ven10](https://github.com/user-attachments/assets/c1675e05-20d3-489e-aa03-83ebbd6701df)





Obteniendo así de las diferentes ventanas la Transformada de Fourier y el espcetro de frecuencias.
![fft1](https://github.com/user-attachments/assets/0a10a6ed-4fb1-4392-8828-752ec0f5a223)
![fft2](https://github.com/user-attachments/assets/9ae7dcca-763b-4c25-817c-1019dccb2087)
![fft3](https://github.com/user-attachments/assets/1b2f981b-859e-4c39-8710-da67768c2fd0)
![fft4](https://github.com/user-attachments/assets/fa0f13c0-a882-434d-8dcc-392a1b3d548d)
![fft5](https://github.com/user-attachments/assets/1358b684-0273-4f81-8d0b-7fe1a7d8a98c)
![fft6](https://github.com/user-attachments/assets/b5179904-7d70-448e-9b8e-0ef15cb4b374)
![fft7](https://github.com/user-attachments/assets/6e4adaab-e699-4f55-96b0-7e82e1ade178)
![fft8](https://github.com/user-attachments/assets/20c5ba17-880a-4c48-90ea-aa9f956c77f1)
![fft9](https://github.com/user-attachments/assets/e8c24102-3978-4e63-abde-bdd0230bcedc)
![fft10](https://github.com/user-attachments/assets/79103d5d-7205-4fa1-92e1-a88a3cba832f)


Tambien se obtuvo el analisis estadistico de cada ventana por medio del test de hipotesis, en este caso usamos la grafica de dos colas.












