from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def main():
    try:
        driver.get("https://www.google.ru/")
    except Exception as e:
        print(e)
    else:
        login()
    finally:
        pass


def login():
    try:
        enter_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="gb_70"]'))
        )
        enter_button.click()
    except Exception as e:
        print(e)
    else:
        enter_data()
    finally:
        pass


def enter_data():
    try:
        EMAIL = "oleg.mustangov90@gmail.com"
        PASSWORD = "99hitugi99"
        input_ = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "identifierId"))
        )
        input_.send_keys(EMAIL)  # Ввод мыла
        input_.send_keys(Keys.ENTER)  # Кнопка "Enter"

        input_ = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        input_.send_keys(PASSWORD)  # Ввод пароля
        input_.send_keys(Keys.ENTER)  # Кнопка "Enter"
    except Exception as e:
        print(e)
    else:
        pass
    finally:
        pass


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome(options=options)
    main()
