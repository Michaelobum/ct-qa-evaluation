import unittest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from page_objects.loginPage import LoginPage
from user_data_utils import load_user_data
from url_proyecto import url
import time

class ProfileTest(unittest.TestCase):

    def setUp(self):
        """Configuración inicial antes de cada prueba
        """
        self.driver = self.initialize_headless_driver()

    def initialize_headless_driver(self):
        """Inicializa y devuelve un WebDriver sin interfaz gráfica
        """
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        return WebDriver(options=options)

        
    def test_profile_process(self):
        self.driver.get(url) # Navegar a la URL
        login_page = LoginPage(self.driver) # Crear una instancia de LoginPage
        login_page.click_login()
        user_data = load_user_data()
        email = user_data['email']
        password = user_data['password']
        login_page.enter_email(email)
        login_page.enter_password(password)
        login_page.click_save_login()

        # Manejar posibles errores de inicio de sesión
        error_message = "These credentials do not match our records."
        if error_message in login_page.message():
            self.fail(f"Fallo en la prueba: Se encontró el mensaje de error de credenciales: {error_message}")

        # Navegar al perfil y realizar acciones en la página de perfil
        login_page.navigate_to_profile()
        login_page.click_profile()
        time.sleep(3)

    def tearDown(self):
        """Cerrar el navegador después de cada prueba
        """
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
