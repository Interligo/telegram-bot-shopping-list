import requests
import json
from aiogram.utils.markdown import text
# Импорт файла с настройками
from sl_db_settings import URL, HEADERS


def show_sl():
    """ Функция показывает весь список покупок """
    response = requests.request("GET", URL, headers=HEADERS)
    products_count = len(response.json())
    text_from_db = 'Список покупок:\n\n'
    # Проверка на пустоту списка покупок
    if not response.json():
        return 'Список покупок пуст. Добавим что-нибудь?'
    else:
        for i in range(products_count):
            text_from_db += text(response.json()[i]['Category'], ': ', response.json()[i]['Product'], ' ',
                                 response.json()[i]['Amount'], ' шт.', sep='')
            text_from_db += '\n'
        text_from_db += '\nДобавим что-нибудь в список?'
        return text_from_db


def add_to_sl(product_name: str, product_amount: str, product_type: str):
    """ Функция добавляет новый объект в БД (название и количество - обязательные поля) """
    product_name = product_name.lower()
    product_type = product_type.capitalize()
    if product_type not in ('Алкоголь', 'Продукты', 'Овощи/фрукты', 'Вкусняшки', 'Бытовая химия'):
        product_type = 'Другое'
    payload = json.dumps({"Product": product_name, "Amount": product_amount, "Category": product_type})
    response = requests.request("POST", URL, data=payload, headers=HEADERS)
    return f'Записала {product_name} в список. Продолжим?'


def update_name_product(product_name: str, new_product_name: str):
    """ Функция обновляет объект в БД (изменяет наименование) """
    product_name = product_name.lower()
    new_product_name = new_product_name.lower()
    # Формируем запрос для поиска продукта в БД
    search = json.dumps({'Product': {'$regex': product_name}})
    search_url = "https://shoppinglist-c382.restdb.io/rest/shoppinglist?q=" + search
    # Получаем в ответ одну строку с информацией об этом продукте и вытаскиваем ID объекта
    response = requests.request("GET", search_url, headers=HEADERS)
    product_id = response.json()[0]['_id']
    product_amount = response.json()[0]['Amount']
    # Формируем новый запрос, используя ID объекта, для внесения изменений в БД
    url = "https://shoppinglist-c382.restdb.io/rest/shoppinglist/" + product_id
    payload = json.dumps({"Product": new_product_name, "Amount": product_amount})
    response = requests.request("PUT", url, data=payload, headers=HEADERS)
    return f'Я исправила название: {product_name} на {new_product_name}. Что-нибудь ещё сделать?'


def update_amount_product(product_name: str, product_amount: str):
    """ Функция обновляет объект в БД (изменяет количество) """
    product_name = product_name.lower()
    product_amount = int(product_amount)
    # Формируем запрос для поиска продукта в БД
    search = json.dumps({'Product': {'$regex': product_name}})
    search_url = "https://shoppinglist-c382.restdb.io/rest/shoppinglist?q=" + search
    # Получаем в ответ одну строку с информацией об этом продукте и вытаскиваем ID объекта
    response = requests.request("GET", search_url, headers=HEADERS)
    product_id = response.json()[0]['_id']
    # Формируем новый запрос, используя ID объекта, для внесения изменений в БД
    url = "https://shoppinglist-c382.restdb.io/rest/shoppinglist/" + product_id
    payload = json.dumps({"Product": product_name, "Amount": product_amount})
    response = requests.request("PUT", url, data=payload, headers=HEADERS)
    return f'Я изменила количество, теперь оно составляет {product_amount} шт. Что-нибудь ещё?'


def count_up_amount_product(product_name: str):
    """ Функция обновляет объект в БД (изменяет количество на +1) """
    product_name = product_name.lower()
    # Формируем запрос для поиска продукта в БД
    search = json.dumps({'Product': {'$regex': product_name}})
    search_url = "https://shoppinglist-c382.restdb.io/rest/shoppinglist?q=" + search
    # Получаем в ответ одну строку с информацией об этом продукте и вытаскиваем ID объекта
    response = requests.request("GET", search_url, headers=HEADERS)
    product_id = response.json()[0]['_id']
    product_amount = response.json()[0]['Amount']
    product_amount += 1
    # Формируем новый запрос, используя ID объекта, для внесения изменений в БД
    url = "https://shoppinglist-c382.restdb.io/rest/shoppinglist/" + product_id
    payload = json.dumps({"Product": product_name, "Amount": product_amount})
    response = requests.request("PUT", url, data=payload, headers=HEADERS)
    return f'Я увеличила количество на один, теперь оно составляет {product_amount} шт. Что-нибудь ещё?'


def update_type_product(product_name: str, new_product_type: str):
    """ Функция обновляет объект в БД (изменяет категорию) """
    # Конструкция для перевода callback на русский
    type_list_eng = ["food", "vegetables", "delicious", "chemicals", "alcohol", "another"]
    type_list_ru = ["Продукты", "Овощи/фрукты", "Вкусняшки", "Бытовая химия", "Алкоголь", "Другое"]
    for eng, ru in zip(type_list_eng, type_list_ru):
        if new_product_type in eng:
            new_product_type = ru
    product_name = product_name.lower()
    # Формируем запрос для поиска продукта в БД
    search = json.dumps({'Product': {'$regex': product_name}})
    search_url = "https://shoppinglist-c382.restdb.io/rest/shoppinglist?q=" + search
    # Получаем в ответ одну строку с информацией об этом продукте и вытаскиваем ID объекта
    response = requests.request("GET", search_url, headers=HEADERS)
    product_id = response.json()[0]['_id']
    product_amount = response.json()[0]['Amount']
    # Формируем новый запрос, используя ID объекта, для внесения изменений в БД
    url = "https://shoppinglist-c382.restdb.io/rest/shoppinglist/" + product_id
    payload = json.dumps({"Product": product_name, "Amount": product_amount, "Category": new_product_type})
    response = requests.request("PUT", url, data=payload, headers=HEADERS)
    new_product_type = new_product_type.lower()
    return f'Я исправила категорию {product_name} на {new_product_type}. Чем ещё могу помочь?'


def delete_from_sl(product_name: str):
    """ Функция удаляет объект из БД """
    product_name = product_name.lower()
    # Формируем запрос для поиска продукта в БД
    search = json.dumps({'Product': {'$regex': product_name}})
    search_url = "https://shoppinglist-c382.restdb.io/rest/shoppinglist?q=" + search
    # Получаем в ответ одну строку с информацией об этом продукте и вытаскиваем ID объекта
    response = requests.request("GET", search_url, headers=HEADERS)
    product_id = response.json()[0]['_id']
    # Формируем новый запрос, используя ID объекта, для внесения изменений в БД
    url = "https://shoppinglist-c382.restdb.io/rest/shoppinglist/" + product_id
    response = requests.request("DELETE", url, headers=HEADERS)
    return f'Убрала {product_name} из списка. Что-нибудь ещё?'


def clear_sl():
    """ Функция очищает БД """
    url = "https://shoppinglist-c382.restdb.io/rest/shoppinglist/*?q={}"
    response = requests.request("DELETE", url, headers=HEADERS)
    return 'Очистила список... Возвращайся скорее. Я буду скучать!'


def search_product_in_sl(product_name: str):
    """ Функция ищет объект в БД и возвращает True/False"""
    product_name = product_name.lower()
    # Формируем запрос для поиска продукта в БД
    search = json.dumps({'Product': {'$regex': product_name}})
    search_url = "https://shoppinglist-c382.restdb.io/rest/shoppinglist?q=" + search
    # Получаем в ответ одну строку с информацией об этом продукте и проверяем пуста она или нет
    response = requests.request("GET", search_url, headers=HEADERS)
    if not response.json():
        return False
    else:
        return True


def search_last_product_in_sl():
    """ Функция находит последний добавленный продукт и возвращает наименование продукта """
    url = "https://shoppinglist-c382.restdb.io/rest/shoppinglist?metafields=true"  # URL с доступом к "_created"
    response = requests.request("GET", url, headers=HEADERS)
    products_count = len(response.json())
    last_product_time = '2020-01-01T00:00:00.576Z'
    last_product_name = ''
    if not response.json():
        return 'Список покупок пуст.'
    else:
        for i in range(products_count):
            if last_product_time < response.json()[i]["_created"]:
                last_product_name = response.json()[i]["Product"]
        return last_product_name
