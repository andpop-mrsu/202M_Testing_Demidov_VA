from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Путь к chromedriver
chromedriver_path = 'D:\\Labs\\POP\\chromedriver.exe'  # Укажите путь к вашему chromedriver
service = ChromeService(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

# Открытие сайта Alibaba.com
try:
    driver.get("https://www.alibaba.com")
    driver.maximize_window()
except Exception as e:
    print(f"Ошибка при открытии сайта: {e}")
else:
    print("Сайт успешно открыт.")

# Тест-кейс 1: Поиск товара по ключевому слову
try:
    search_box = driver.find_element(By.CLASS_NAME, "search-bar-input")
    search_box.send_keys("laptop")
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)  # Ожидание загрузки результатов
    results = driver.find_elements(By.ID, "sse-fluent-offerlist")
    assert len(results) > 0, "Результаты поиска не найдены"
except Exception as e:
    print(f"Ошибка в тест-кейсе 1: {e}")
else:
    print("Тест-кейс 1 успешно выполнен.")

# Тест-кейс 2: Добавление товара в корзину
try:
    # Переход на страницу товара (замените URL на реальный)
    driver.get("https://www.alibaba.com/product-detail/OEM-Core-I7-Laptop-Brand-New_1601168798399.html?spm=a2700.galleryofferlist.normal_offer.d_title.1ba913a0gy9ja8")
    time.sleep(3)  # Ожидание загрузки страницы товара

    add_quantity_button = driver.find_element(By.CSS_SELECTOR, ".number-picker-button:nth-child(4)>.id-translate-y-\\[-1px\\]").click()
    # Добавление товара в корзину
    add_to_cart_button = driver.find_element(By.CLASS_NAME, "id-line-clamp-2").click()

    # Переход в корзину
    time.sleep(3)
    cart_icon = driver.find_element(By.CLASS_NAME, "tnh-badge").click()

    # Проверка наличия товара в корзине
    time.sleep(3)
    cart_items = driver.find_elements(By.CLASS_NAME, "sc-shopping-cart-valid-list")
    assert len(cart_items) > 0, "Товар не добавлен в корзину"
except Exception as e:
    print(f"Ошибка в тест-кейсе 2: {e}")
else:
    print("Тест-кейс 2 успешно выполнен.")

# Тест-кейс 3: Попытка поиска без ключевого слова
try:
    driver.get("https://www.alibaba.com")
    search_box = driver.find_element(By.CLASS_NAME, "search-bar-input")
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)  # Ожидание загрузки результатов
    error_message = driver.find_elements(By.ID, "sse-fluent-offerlist")
    assert len(error_message) > 0, "Система выполнила пустой поиск"
except Exception as e:
    print(f"Ошибка в тест-кейсе 3: {e}")
else:
    print("Тест-кейс 3 успешно выполнен.")

# Тест-кейс 4: Попытка добавления товара в корзину с недопустимым количеством
try:
    # Переход на страницу товара (замените URL на реальный)
    driver.get("https://www.alibaba.com/product-detail/OEM-Core-I7-Laptop-Brand-New_1601168798399.html?spm=a2700.galleryofferlist.normal_offer.d_title.1ba913a0gy9ja8")
    time.sleep(5)  # Ожидание загрузки страницы товара

    # Указание недопустимого количества
    quantity_field = driver.find_element(By.CSS_SELECTOR, ".ui-number-picker>input")
    quantity_field.send_keys("99999999999")

    # Попытка добавления в корзину
    add_to_cart_button = driver.find_element(By.CLASS_NAME, "id-line-clamp-2").click()

    cart_icon = driver.find_element(By.CLASS_NAME, "tnh-badge").click()

    # Проверка сообщения об ошибке
    time.sleep(5)

    check = get_attribute.driver.find_element(By.CSS_SELECTOR, ".next-input-group>input")

    assert len(check) == 99999999999, "Система разрешила добавление товара с недопустимым количеством"
except Exception as e:
    print(f"Ошибка в тест-кейсе 4: {e}")
else:
    print("Тест-кейс 4 успешно выполнен.")

# Закрытие браузера
driver.quit()
print("Скрипт завершён.")