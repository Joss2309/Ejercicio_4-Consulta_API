#Practica_Programada_3_Scraping
#Joselyn_Martinez_Arias
#Curso_Nayid_Programación

#Primero Importe librerias

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By



#El URL de la pagina principal donde se extraera los datos

pagina_principal = "https://www.scrapethissite.com/pages/forms/"

#Inicio busqueda en el navegador chrome, ingreso a la página del URL 
#solicito unaa espera de 10 segundos para que los elementos carguen
navegador = webdriver.Chrome()
navegador.get(pagina_principal)  # Abre la página web especificada por la URL.
navegador.implicitly_wait(10) 

# Le indico una lista vacía de datos que luego me va a almacenar la información que deseo.
# Lo que investigue la segunda línea 27 le indico que los datos equipo, desde el navegador 
# controlado por Selenium, realice la busqueda de los datos de la pagina  web, donde le especifico 
# que me busque el nombre de clase CSS. y yo desde la pagina averigue era team, para que me los seleccione y 
# me los forme en una lista.
datos = []
equipos = navegador.find_elements(By.CLASS_NAME, 'team')

# El for entendí es un bucle que repite todas las instrucciones que le indico sobre cada lista de equipos,
# y este dentro de equipos, con la clase css y me  extraiga  la información que realice como lista de dicionario.
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

# Utilice el append para añadir un la lista que ya cree y me construya cada elemento
# para extraer información de la web, la información que deseo en una lista.    
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
