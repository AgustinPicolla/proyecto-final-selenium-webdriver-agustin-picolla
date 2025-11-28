# tests/test_footer.py

from page.login_page import LoginPage
from page.footer_page import FooterPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_footer_twitter_redirect(driver):
    login = LoginPage(driver)
    footer = FooterPage(driver)

    # Login
    login.open()
    login.login("standard_user", "secret_sauce")

    # Click en Twitter (abre nueva pestaña)
    footer.click_twitter()

    # Esperar a que haya 2 pestañas
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) == 2)

    # Cambiar a la nueva pestaña
    new_tab = driver.window_handles[1]
    driver.switch_to.window(new_tab)

    # Validar URL destino (X.com)
    WebDriverWait(driver, 10).until(
        EC.url_contains("x.com")
    )

    assert "x.com" in driver.current_url
