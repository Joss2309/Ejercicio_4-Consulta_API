import json 
import requests 
from requests.auth import HTTPBasicAuth

URL = "https://my.sportmonks.com/login"

#Autenticación de crear usurario y contraseña
email = 'psarias23@gmail.com'
contraseña = '230991'

#Realizar la consulta GET a la autenticación con REQUESTS
respuesta = requests.get(URL, auth=HTTPBasicAuth(email, contraseña))

if respuesta.status_code == 200:
    print('Solicitud exitosa')
    print('Datos:', respuesta.json())
else:
    print("Error en la solicitud del recurso. Detalles: \n",
          respuesta.text)
