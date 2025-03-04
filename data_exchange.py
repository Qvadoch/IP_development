import json
import os
from users import User
from admins import Admin
from flowers import Flower

class DataExchange():
    @staticmethod
    def import_data(users: list, flowers: list, admins: list):
        filename = input("Введите имя файла для импорта: ")
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for user_data in data['users']:
                    user = User(user_data['username'], user_data['password'])
                    users.append(user)
                for admin_data in data['admins']:
                    admin = Admin(admin_data['username'], admin_data['password'])
                    admins.append(admin)
                for flower_data in data['flowers']:
                    flower = Flower(flower_data['name'], flower_data['price'])
                    flowers.append(flower)
                print("Данные успешно импортированы")
        except Exception as e:
            print(f"Ошибка при импорте данных: {e}")

    @staticmethod
    def export_data(users: list, flowers: list, admins: list):
        filename = input("Введите название файла для экспорта: ")
        data = {
            'users': [{'username': user.username, 'password': user.password} for user in users],
            'flowers': [{'name': flower.name, 'price': flower.price} for flower in flowers],
            'admins':[{'username': admin.username, 'password': admin.password} for admin in admins],
        }
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
                print("Данные успешно экспортированы!")
        except Exception as e:
            print(f"Ошибка при экспорте данных: {e}")

    @staticmethod
    def begin_import_data(users: list, flowers: list, admins: list):

        filename = "Файл.json"
        
        if not os.path.exists(filename):
        
            initial_data = {
                "users": [],
                "admins": [],
                "flowers": []
            }
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(initial_data, file, ensure_ascii=False, indent=4)
            print(f"Файл {filename} создан с начальными данными.")
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for user_data in data['users']:
                    user = User(user_data['username'], user_data['password'])
                    users.append(user)
                for admin_data in data['admins']:
                    admin = Admin(admin_data['username'], admin_data['password'])
                    admins.append(admin)
                for flower_data in data['flowers']:
                    flower = Flower(flower_data['name'], flower_data['price'])
                    flowers.append(flower)
                print("Данные успешно импортированы")
        except Exception as e:
            print(f"Ошибка при импорте данных: {e}")
    