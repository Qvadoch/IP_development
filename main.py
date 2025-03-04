from admins import Admin
from users import User
from flowers import Flower
from menus import Menu
from data_exchange import DataExchange
from personality import Personality

flowers = [
    Flower("Роза", 25),
    Flower("Тюльпан", 30),
    Flower("Лилия", 45)
]
users = []
admins = []

def display_personality_info(personality: Personality):
        "Функция для демонстрации полиморфизма."
        personality.display_info()

def main():
    DataExchange.begin_import_data(users, flowers, admins)
    while True:
        action = input("Хотите создать новый логин и пароль (1) или войти под существующим (2)? Выход из программы(3): ").strip().upper()

        if action == "1":
            role_choice = input("Выберите роль (1 - пользователь, 2 - администратор): ").strip()
            if role_choice == "1":
                User.create_user(users)
                DataExchange.export_data(users, flowers, admins)
            elif role_choice == "2":
                Admin.create_admin(admins)
                DataExchange.export_data(users, flowers, admins)
            else:
                print("Неверный выбор роли.")

        elif action == "2":
            if not users and not admins:
                print("Нет зарегистрированных пользователей или администраторов.")
                continue

            username = input("Логин: ")
            password = input("Пароль: ")
            role = input("Введите роль (user/admin): ").strip().lower()

            if role == "user":
                for user in users:
                    if user.username == username and user.password == password:
                        display_personality_info(user)
                        Menu.user_menu(user, flowers, users, admins)
                        DataExchange.export_data(users, flowers, admins)
                        break
                else:
                    print("Неверный логин или пароль.")
            elif role == "admin":
                for admin in admins:
                    if admin.username == username and admin.password == password:
                        display_personality_info(admin)
                        Menu.admin_menu(admin, flowers, users, admins)
                        DataExchange.export_data(users, flowers, admins)
                        break
                else:
                    print("Неверный логин или пароль.")
            else:
                print("Неверная роль.")

        elif action == "3":
            return

        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()