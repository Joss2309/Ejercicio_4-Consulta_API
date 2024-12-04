# importamos librerias
import requests


#consumir el recurso de la pagina
URL = "https://api.lambdatest.com/automation/api/v1/platforms"



# Realizar la solicitud GET a la API 
respuesta = requests.get(URL)

# Verificar el estado de la solicitud
if respuesta.status_code == 200:
    print('Su solicitud fue exitosa')
    print('Datos: ', respuesta.json())
else:
    print('Error en la solicitud. Detalles: \n', respuesta.text)

