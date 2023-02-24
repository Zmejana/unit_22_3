import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from settings import valid_email, valid_password


driver = webdriver.Chrome()


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('//chromedriver_directory/chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()


@pytest.fixture()
def test_show_my_pets():
   # Вводим email
   pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Нажимаем на ссылку "Мои питомцы"
   pytest.driver.find_element(By.LINK_TEXT, "Мои питомцы").click()
