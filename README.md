#Проект над виджетом банковских операций клиента

Описание:

Проект реализует функции:

mask_account_card: принимает строку, содержащую тип и номер карты или счета. Возвращает строку с замаскированным номером карты/счета get_date: принимает строку с датой в формате iso 8601. Возвращает строку с датой в формате ДД.ММ.ГГГГ filter_by_state, которая принимает на вход список словарей с данными о банковских операциях и параметр state, возвращает новый список, содержащий только те словари, у которых ключ state содержит переданное в функцию значение. sort_by_date, которая принимает на вход список словарей и параметр порядка сортировки, возвращает новый список, в котором исходные словари отсортированы по дате. filter_by_currency, которая принимает на вход список словарей, представляющих транзакции. Функция должна возвращать итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной.

Проект дополнен генераторами

transaction_descriptions, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди. card_number_generator, который выдает номера банковских карт в заданном формате. Также генератор может сгенерировать номера карт в заданном диапазоне.

Проект дополнен декоратором 
Декоратор log принимает необязательный аргумент filename, который определяет имя файла, в который будут записываться логи

#Документация описание будет добавлено позже
