import pytest

# @pytest.mark.parametrize("x", [-1, 0, 1], ids=["negative", "zero", "positive"])
# @pytest.mark.parametrize("y", [100, 1000], ids=["3 digit", "4 digit"])
# def test_multiply_params(x, y):
#    print("x: {0}, y: {1}".format(x, y))
#    assert True

from api import PetFriends
from settings import valid_email, valid_password
import os
import requests
import json


pf = PetFriends()

@pytest.fixture(autouse=True)
def ket_api_key():
   """ Проверяем, что запрос api-ключа возвращает статус 200 и в результате содержится слово key"""

   # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
   status, pytest.key = pf.get_api_key(valid_email, valid_password)

   # Сверяем полученные данные с нашими ожиданиями
   assert status == 200
   assert 'key' in pytest.key

   yield

   # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
   assert status == 200

def generate_string(n):
   return "x" * n

def russian_chars():
   return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

# Здесь мы взяли 20 популярных китайских иероглифов
def chinese_chars():
   return '的一是不了人我在有他这为之大来以个中上们'

def special_chars():
   return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'

@pytest.mark.parametrize("name", [
   ''
   , generate_string(255)
   , generate_string(1001)
   , russian_chars()
   , russian_chars().upper()
   , chinese_chars()
   , special_chars()
   , '123'
], ids=[
   'empty'
   , '255 symbols'
   , 'more than 1000 symbols'
   , 'russian'
   , 'RUSSIAN'
   , 'chinese'
   , 'specials'
   , 'digit'
])
def test_add_new_pet_simple(name, animal_type='двортерьер',
                           age='4'):
   """Проверяем, что можно добавить питомца с различными данными"""

   # Добавляем питомца
   status, result = pf.add_new_pet_simple(pytest.key, name, animal_type, age)

   # Сверяем полученный ответ с ожидаемым результатом
   if name == '':
      assert status == 400
   else:
      assert status == 200
      assert result['name'] == name
      assert result['age'] == age
      assert result['animal_type'] == animal_type
