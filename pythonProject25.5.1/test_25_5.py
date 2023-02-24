from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()

pets = driver.find_elements(By.TAG_NAME, 'tr')
images = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
names = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
descriptions = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')


def test_pet_table(test_show_my_pets):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div > div[class=".col-sm-4 left"]'))
    )
    for i in element:
        numb = i.text.split('\n')
        number = numb[1].split(' ')
        numbers = int(number[1])
        assert len(pets) in numbers

    assert len(images) >= len(pets) // 2

    current = [names[i] for i in range(len(names))]
    setcar = set(current)
    assert len(current) == len(setcar)

    sum = [names[i] for i in range(len(pets))]
    setcum = set(sum)
    assert len(sum) == len(setcum)


def test_pet_cards(test_show_my_pets):
    driver.implicitly_wait(10)
    myDynamicElementsPhoto = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    myDynamicElementsName = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    myDynamicElementsAge = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')
    assert len(myDynamicElementsPhoto) >= len(pets) // 2

    assert len(pets) == len(myDynamicElementsName)
    for i in range(len(myDynamicElementsAge)):
        assert ', ' in myDynamicElementsAge
        parts = myDynamicElementsAge[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0
