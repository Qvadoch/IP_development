from users import User
from admins import Admin
from flowers import Flower
from data_exchange import DataExchange
from data_exchange import DataExchange

class Menu():
    @staticmethod
    def user_menu(user: User, flowers: list[Flower], users: list[User], admins: list[Admin]):
        while True:
            print(f"\n--- Пользовательское меню {user.username}---")
            print("1. Просмотреть доступные цветы")
            print("2. Купить цветы")
            print("3. Просмотреть историю покупок")
            print("4. Обновить профиль")
            print("5. Выйти")

            choice = input("Выберите действие: ")

            if choice == "1":
                User.view_flowers(flowers)
            elif choice == "2":
                user.buy_flower(flowers)
                DataExchange.export_data(users, flowers, admins)
            elif choice == "3":
                user.view_history()
            elif choice == "4":
                user.update_profile()
                DataExchange.export_data(users, flowers, admins)
            elif choice == "5":
                break
            else:
                print("Неверный выбор, попробуйте снова.")

    @staticmethod
    def admin_menu(admin: Admin, flowers: list[Flower], users: list[User], admins: list[Admin]):
        while True:
            print(f"\n--- Пользовательское меню {admin.username}---")
            print("1. Добавить цветок")
            print("2. Удалить цветок")
            print("3. Обновить цветок")
            print("4. Просмотреть всех пользователей")
            print("5. Создать нового администратора")
            print("6. Сортировать цветы")
            print("7. Фильтровать цветы по цене")
            print("8. Экспортировать данные")
            print("9. Импортировать данные")
            print("10. Выйти")

            choice = input("Выберите действие: ")

            if choice == "1":
                admin.add_flower(flowers)
                DataExchange.export_data(users, flowers, admins)
            elif choice == "2":
                admin.remove_flower(flowers)
                DataExchange.export_data(users, flowers, admins)
            elif choice == "3":
                admin.update_flower(flowers)
                DataExchange.export_data(users, flowers, admins)
            elif choice == "4":
                admin.view_users(users)
            elif choice == "5":
                Admin.create_admin(admins)
                DataExchange.export_data(users, flowers, admins)
            elif choice == "6":
                admin.sort_flowers(flowers)
            elif choice == "7":
                admin.filter_flowers(flowers)
            elif choice == "8":
                DataExchange.export_data(users, flowers, admins)
            elif choice == "9":
                DataExchange.import_data(users, flowers, admins)
            elif choice == "10":
                break
            else:
                print("Неверный выбор, попробуйте снова.")