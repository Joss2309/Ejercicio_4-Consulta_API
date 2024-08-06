#Practica_Programada_3_Scraping
#Joselyn_Martinez_Arias
#Curso_Nayid_Programación

#Primero Importe librerias

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By



#El URL de la pagina principal donde se extraera los datos

pagina_principal = "https://www.scrapethissite.com/pages/forms/"

#Inicio busqueda en el navegador chrome, ingresar a la página del URL y dar un espera de 10 segundos para que los eleentos carguen
navegador = webdriver.Chrome()
navegador.get(pagina_principal)  # Abre la página web especificada por la URL.
navegador.implicitly_wait(10) 

datos = []
equipos = navegador.find_elements(By.CLASS_NAME, 'team')

for equipo in equipos:
    nombre = equipo.find_element(By.CLASS_NAME, "name").text
    anio = equipo.find_element(By.CLASS_NAME, "year").text
    victorias = equipo.find_element(By.CLASS_NAME, "wins").text
    derrotas = equipo.find_element(By.CLASS_NAME, "losses").text
    derrotas_tiempo_extra = equipo.find_element(By.CLASS_NAME, "ot-losses").text
    porcentaje_victorias = equipo.find_element(By.CLASS_NAME, "pct").text
    goles_favor = equipo.find_element(By.CLASS_NAME, "gf").text
    goles_contra = equipo.find_element(By.CLASS_NAME, "ga").text
    gol_diferencia = equipo.find_element(By.CLASS_NAME, "diff").text
    
    datos.append({
        'NOMBRE' : nombre,
        'AÑO' : anio,
        'VICTORIAS' : victorias,
        'DERROTAS' : derrotas,
        'DERROTAS_TIEMPO_EXTRA' : derrotas_tiempo_extra,
        'GOLES_FAVOR' : goles_favor,
        'GOLES_CONTRA' : goles_contra,
        'GOL_DIFERENCIA' : gol_diferencia
        })
   
navegador.quit()
df = pd.DataFrame(datos)
print(df)

ruta = "C:/Users/Usuario/Desktop/Joselyn/Curso Analisis de Datos/Tercer Cuatrimestre/Taller de Programación para analisis de datos II Nayid Vargas/Practica_Programada3_Scraping"

df.to_excel(ruta + "Datos proyecto.xlsx",index =False)
