import unittest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from page_objects.loginPage import LoginPage
from utils.user_data_utils import load_user_data
from utils.url_proyecto import url

class LogOutTest(unittest.TestCase):

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

    def test_logout_process(self):
        # Iniciar el navegador y abrir la URL del proyecto
        self.driver.get(url)
        
        # Iniciar sesión con credenciales
        login_page = LoginPage(self.driver)
        user_data = load_user_data()
        email, password = user_data['email'], user_data['password']
        login_page.login(email, password)

        # Manejar posibles errores de inicio de sesión
        error_message = "These credentials do not match our records."
        if error_message in login_page.message():
            self.fail(f"Fallo en la prueba: Se encontró el mensaje de error de credenciales: {error_message}")

        # Navegar al perfil y realizar acciones en la página de perfil
        login_page.navigate_to_profile()
        login_page.click_logout()

    def tearDown(self):
        """Cerrar el navegador después de cada prueba
        """
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
