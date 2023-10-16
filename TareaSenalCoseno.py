import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal portadora
amplitud_portadora = 1.0
frecuencia_portadora = 1000  # Hz
periodo_portadora = 1.0 / frecuencia_portadora

# Parámetros de la señal de mensaje
frecuencia_mensaje = 10  # Hz
periodo_mensaje = 1.0 / frecuencia_mensaje

# Tiempo de muestreo
tiempo_muestreo = 0.001  # 1 ms
t = np.arange(0, 1, tiempo_muestreo)

# Generar la señal de mensaje (una señal sinusoidal)
mensaje = np.sin(2 * np.pi * frecuencia_mensaje * t)

# Modulación de amplitud (AM)
señal_modulada = amplitud_portadora * np.cos(2 * np.pi * frecuencia_portadora * t + mensaje)

# Graficar la señal de mensaje
plt.figure(figsize=(10, 4))
plt.subplot(311)
plt.plot(t, mensaje)
plt.title('Señal de Mensaje')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

# Graficar la señal portadora
plt.subplot(312)
plt.plot(t, amplitud_portadora * np.cos(2 * np.pi * frecuencia_portadora * t))
plt.title('Señal Portadora')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

# Graficar la señal modulada
plt.subplot(313)
plt.plot(t, señal_modulada)
plt.title('Señal Modulada')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

plt.tight_layout()
plt.show()
