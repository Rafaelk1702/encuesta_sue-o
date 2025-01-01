import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Generar poblacion
poblacion = np.arange(1,13000)

#Seleccionar porcentaje
porcentaje1 = 39  # Porcentaje que deseas seleccionar
porcentaje2 = 28
elementos_1 = int(len(poblacion) * (porcentaje1 / 100))
elementos_2 = int(len(poblacion) * (porcentaje2 / 100))
# Seleccionar los primeros n_elementos del vector
# seleccion = poblacion[:elementos_1]



#2019 vs 2020 para dormir mejor
# print(elementos_1)
# print(elementos_2)

anios = ["2019","2020"]
leer_para_dormir_mejor = [elementos_1, elementos_2]
plt.plot(anios, leer_para_dormir_mejor, label="Leer",color="purple", marker="*")
plt.xlabel("Año")
plt.ylabel("Adultos")

plt.title("Los resultados de la V Encuesta del Sueño, realizada por Royal Philips.\nEstrategias antes de acostarse")
plt.xticks(np.arange(-1,3))
plt.yticks(np.arange(0, elementos_1+elementos_2, 500))
# plt.yticks(np.arange(min(leer_para_dormir_mejor), max(leer_para_dormir_mejor)+1, 1.0))
#texto en plot
plt.annotate(str(porcentaje1)+'%', xy=(0,5500), xytext=(0,5500))
plt.annotate(str(porcentaje2)+'%', xy=(1,4000), xytext=(1,4000))
plt.grid(visible="Active")
#Activar Legenda
plt.legend()

#colocar texto

# bar_container = plt.bar(ages, leer_para_dormir_mejor)
# plt._label(bar_container, fmt=lambda x: f'{x * 1.61:.1f} km/h'

plt.show()
# print(leer_para_dormir_mejor)

#////////////////////////////////////////////
#Llamada de atención: tendencias globales de satisfacción del sueño

porcentaje1 = 49  
porcentaje2 = 33
porcentaje3 = 18
total = 100

plt.bar(0.2, porcentaje1, width=1/5, label="Están satisfechas con su sueño")
plt.bar(0.4, porcentaje2, width=1/5,label="Preocupación y estrés afecta conciliar el sueño")
plt.bar(0.6, porcentaje3, width=1/5,label="Otros factores afectan conciliar el sueño")
plt.xlabel("Grupos de personas")
plt.ylabel("Porcentaje")
plt.title("Llamada de atención: tendencias globales de satisfacción del sueño")
plt.xticks(np.arange(0.8,0.8))
plt.yticks(np.arange(0, total+10, 10))
# plt.annotate(str(porcentaje1)+'%', xy=(0.18,50), xytext=(0.18,50))
plt.grid(visible="Active")
plt.legend()
plt.show()




#////////////////////////////////////////////
#Problemas de sueño entre parejas
#Seleccionar porcentaje
porcentaje4 = 36  # 36% de las personas con una pareja está de acuerdo en que a veces duermen por separado para mejorar el sueño
porcentaje5 = 33  # 30% confirma que la dificultad para dormir de su compañero está afectando directamente a su relación
porcentaje6 = 39  # Las personas que usan los móviles
porcentaje7 = 10  # Porcentaje con Apnea de sueño
total = 100
plt.bar(0.2, porcentaje4, width=1/6, label="Parejas: Están de acuerdo en que a veces duermen por separado")
plt.bar(0.4, porcentaje5, width=1/6,label="Parejas: La dificultad para dormir de su compañero está afectando\n directamente a su relación")
plt.bar(0.6, porcentaje6, width=1/6,label="Cuatro de cada diez, usan sus móviles (antes de dormir o al levantarse)")
plt.bar(0.8, porcentaje7, width=1/6,label="Apnea del sueño")
plt.xlabel("Grupos de personas")
plt.ylabel("Porcentaje")
plt.title("Los factores que ponen en riesgo la calidad del sueño son tanto sociales como tecnológicos.")
plt.xticks(np.arange(0.8,0.8))
plt.yticks(np.arange(0, total+10, 10))
plt.grid(visible="Active")
plt.legend()
plt.show()

#Fuentes:
#https://www.consalud.es/pacientes/encuesta-philips-mitad-poblacion-satisfecha-sueno_75200_102.html