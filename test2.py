from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

# Definir la URL de login
url_login = "https://playamar.wodbuster.com/user/login.aspx"

# Definir los datos de login
usuario = "lauralangone@hotmail.com"
contrasena = "Lan001260/*"

# Iniciar el navegador web
driver = webdriver.Chrome()

# Acceder a la página de login
driver.get(url_login)

# Buscar los elementos del formulario
username_field = driver.find_element(By.ID, "body_body_CtlLogin_IoEmail")
password_field = driver.find_element(By.ID, "body_body_CtlLogin_IoPassword")
login_button = driver.find_element(By.ID, "body_body_CtlLogin_CtlAceptar")

# Introducir los datos de login
username_field.send_keys(usuario)
password_field.send_keys(contrasena)

# Hacer clic en el botón de login
login_button.click()

# Esperar a que la página se cargue
driver.implicitly_wait(5)

no_remember_button = driver.find_element(By.ID, "body_body_CtlConfiar_CtlNoSeguro")
no_remember_button.click()

# Esperar a que la página se cargue
driver.implicitly_wait(10)

# 930
#  https://playamar.wodbuster.com/athlete/reservas.aspx?t=1708992000   data-id=i6043


# Verificar si el login fue exitoso
if "Login correcto" in driver.page_source:
    # El login fue exitoso
    print("¡Has iniciado sesión correctamente!")
else:
    # El login falló
    print("Hubo un error al iniciar sesión")

# Cerrar el navegador web
driver.quit()
