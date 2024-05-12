import sys
import requests

# Definir la URL de login
url_login = "https://playamar.wodbuster.com/user/login.aspx"

# Definir los datos de login
usuario = "lauralangone@hotmail.com"
contrasena = "Lan001260/*"

<input type="submit" name="ctl00$ctl00$body$body$CtlLogin$CtlAceptar" value="Aceptar" id="body_body_CtlLogin_CtlAceptar" class="mainsubmit">

# Crear la solicitud POST
payload = {
    "ctl00$MainContent$txtUsuario": usuario,
    "ctl00$MainContent$txtContrasena": contrasena,
    "ctl00$MainContent$btnLogin": "Entrar"
}

# Enviar la solicitud y obtener la respuesta
with requests.Session() as session:
    response = session.post(url_login, data=payload)

# Verificar si el login fue exitoso
if "Login correcto" in response.text:
    # El login fue exitoso
    print("¡Has iniciado sesión correctamente!")
else:
    # El login falló
    print("Hubo un error al iniciar sesión")
    print(response.text)
    sys.exit(1)


# Definir la URL
url = "https://playamar.wodbuster.com/athlete/reservas.aspx?t=1708992000#:~:text=16%3A00-,Entrenar,-CrossFit"

# Hacer la petición GET
response = requests.get(url)

# Verificar el código de respuesta
if response.status_code == 200:
    # La petición fue exitosa
    print("La página web se ha cargado correctamente")
    # Imprimir el contenido de la página
    print(response.content)
else:
    # La petición falló
    print("Hubo un error al cargar la página web")
    print("Código de respuesta:", response.status_code)
