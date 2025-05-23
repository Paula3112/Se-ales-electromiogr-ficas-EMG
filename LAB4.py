import nidaqmx
from nidaqmx.constants import AcquisitionType, READ_ALL_AVAILABLE
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, filtfilt
import datetime

# Función para crear un filtro pasa bajas Butterworth
def butter_lowpass_filter(data, cutoff=100, fs=5000, order=4):
    nyquist = 0.5 * fs  # Frecuencia de Nyquist
    normal_cutoff = cutoff / nyquist  # Frecuencia normalizada
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return filtfilt(b, a, data)

# Crear la tarea de adquisición de datos
with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan("Dev4/ai1")
    task.timing.cfg_samp_clk_timing(5000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=10000)  # 50 muestras a 5 kHz

    data = task.read(READ_ALL_AVAILABLE)  # Leer los datos

    # Convertir la señal a un array de NumPy
    data = np.array(data)

    # Aplicar filtro pasa bajas
    filtered_data = butter_lowpass_filter(data)

    # Graficar la señal original y filtrada
    plt.figure(figsize=(8, 5))
    #plt.plot(data, label="Señal Original", alpha=0.5)
    plt.plot(filtered_data, linewidth=2)
    #plt.ylabel('Amplitud')
   # plt.xlabel('Muestras')
    plt.title('Señal Adquirida')
    plt.legend()
    plt.grid()

    # Guardar la imagen con timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"señal_{timestamp}.png"
    plt.savefig(filename, dpi=300)
    plt.show()
