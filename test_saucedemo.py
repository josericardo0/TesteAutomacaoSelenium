from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 


class PaginaLogin:
    def iniciar(self, driver):
        self.driver = driver

    def login(self, usuario, senha):
        campo_usuario = self.driver.find_element(By.ID, "user-name")
        campo_senha = self.driver.find_element(By.ID, "password")
        botao_login = self.driver.find_element(By.ID, "login-button")

        campo_usuario.send_keys(usuario)
        campo_senha.send_keys(senha)
        botao_login.click()

class PaginaProdutos:
    def iniciar(self, driver):
        self.driver = driver

    def adicionar_ao_carrinho(self, numero_produtos=2):
        botao_adicionar_produto = self.driver.find_elements(By.CLASS_NAME, "btn_inventory")
        for button in botao_adicionar_produto[:numero_produtos]:
            button.click()
            time.sleep(1)

class PaginaDoCarrinho:
    def iniciar(self, driver):
        self.driver = driver

    def ir_para_checkout(self):
        icone_carro = self.driver.find_element(By.CLASS_NAME, "shopping_cart_container")
        icone_carro.click()

class PaginaDeCheckout:
    def iniciar(self, driver):
        self.driver = driver
        
    def clicar_no_botao_de_checkout(self):
        botao_checkout = self.driver.find_element(By.CLASS_NAME, "checkout_button")
        botao_checkout.click()
        
    def preencher_informacoes(self, first_name, last_name, postal_code):
        wait = WebDriverWait(self.driver, 10)
        campo_primeiro_nome= wait.until(EC.presence_of_element_located((By.ID, "first-name")))
        
        campo_ultimo_nome = self.driver.find_element(By.ID, "last-name")
        campo_codigo_postal = self.driver.find_element(By.ID, "postal-code")
        botao_continuar = self.driver.find_element(By.CLASS_NAME, "cart_button")

        campo_primeiro_nome.send_keys(first_name)
        campo_ultimo_nome.send_keys(last_name)
        campo_codigo_postal.send_keys(postal_code)
        botao_continuar.click()
        
    def finalizar_pedido(self):
        wait = WebDriverWait(self.driver, 10)
        botao_finalizar = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
        botao_finalizar.click()


driver = webdriver.Chrome()
driver.maximize_window() 
driver.get("https://www.saucedemo.com")

pagina_login = PaginaLogin()
pagina_login.iniciar(driver)
pagina_login.login("standard_user", "secret_sauce")

pagina_produtos = PaginaProdutos()
pagina_produtos.iniciar(driver)
pagina_produtos.adicionar_ao_carrinho()

pagina_carrinho = PaginaDoCarrinho()
pagina_carrinho.iniciar(driver)
pagina_carrinho.ir_para_checkout()

pagina_checkout = PaginaDeCheckout()
pagina_checkout.iniciar(driver)
pagina_checkout.clicar_no_botao_de_checkout()
pagina_checkout.preencher_informacoes("José", "Ricardo", "12345")
pagina_checkout.finalizar_pedido()

time.sleep(3)
driver.quit()
