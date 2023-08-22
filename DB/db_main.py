import datetime
import sqlite3

import pandas as pd

from DB.DB import cur, con


def add_client(clients_id: int):
    """
    Функция, позволяющая добавить нового клиента
    :param: clients_id - телеграм id клиента
    """
    if cur.fetchone() is None:
        try:
            cur.execute("INSERT INTO clients VALUES (?)", (clients_id,))
            con.commit()
            return 'Новый клиент добавлен'
        except sqlite3.IntegrityError:
            return 'Такой id есть в базе'


# id_client = 111111122222222222


# print(add_client(id_client))


def add_password(password, date):
    """
    Функция, позволяющая добавить новый пароль
    :param: password - пароль пользователя,
            date - автоматическое заполнение даты и времени создания пароля
    """
    if cur.fetchone() is None:
        try:
            cur.execute("INSERT INTO password VALUES (?, ?)", (password, date))
            con.commit()
            return 'Новый пароль добавлен'
        except sqlite3.IntegrityError:
            return 'Такой пароль есть в базе'


# client_password = '2rfvg@@###566'


# print(add_password(client_password, datetime.datetime.now()))


def update_password(password, date):
    """
    Функция обновления имеющегося пароля
    :param: new_password -новый пароль пользователя,
            date - автоматическое заполнение даты и времени создания пароля
    """
    old_password = '2rfvg@@###566'
    if cur.fetchone:
        try:
            password_users = "DELETE FROM password WHERE password = ?"
            cur.execute(password_users, (old_password,))
            con.commit()
            cur.execute("INSERT INTO password VALUES (?, ?)", (password, date))
            con.commit()
            return 'Пароль обновлён'
        except sqlite3.IntegrityError:
            return 'Такой пароль есть в базе'


# new_password = '##@@@@@787ghggvhfgf'


# print(update_password(new_password, datetime.datetime.now()))


def all_id_csv():
    """
    Функция записи id клиентов в csv файл
    """
    file = pd.read_sql('SELECT * from clients', con)
    file.to_csv('clients.csv', index=False)
    return 'id клиентов успешно записаны в файл csv'


# print(all_id_csv())


def delete_password():
    """
    Функция удаления пароля
    """
    del_password = '##@@@@@787ghggvhfgf'
    password_users = "DELETE FROM password WHERE password = ?"
    cur.execute(password_users, (del_password,))
    con.commit()
    return 'Пароль удалён'


# print(delete_password())

def delete_id():
    """
    Функция удаления id клиента
    """
    del_client = 111111122222222222
    clients_id = "DELETE FROM clients WHERE id = ?"
    cur.execute(clients_id, (del_client,))
    con.commit()
    return 'id клиента удалён'


# print(delete_id())


def list_id():
    """
    Функция
    :return: список id клиентов
    """
    list_id_clients = []
    id_clients = cur.execute("SELECT * FROM clients").fetchall()
    for _id in id_clients:
        for item in _id:
            list_id_clients.append(item)
    return list_id_clients


# print(list_id())
