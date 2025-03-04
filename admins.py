from personality import Personality
from users import User
from flowers import Flower

class Admin(Personality):
    def __init__(self, username: str, password: str):
        super().__init__(username, password, role="admin")

    def display_info(self):
        print(f"Администратор: {self.username}, Роль: {self.role}")
        
    @staticmethod
    def create_admin(admins: list):
        new_admin = input("Введите логин администратора: ")
        new_password = input("Введите пароль администратора: ")

        if not new_admin.strip() or not new_password.strip():
            print("Логин и пароль не могут быть пустыми.")
            return

        for admin in admins:
            if admin.username == new_admin  and admin.role == "admin":
                print("Администратор с таким логином уже существует!")
                return

        save_new_admin = Admin(new_admin, new_password)
        admins.append(save_new_admin)
        print(f"Администратор '{new_admin}' успешно создан!")

    def add_flower(self, flowers: list[Flower]):
        name = input("Введите название цветка: ")
        if not name.strip():
            print("Название цветка не может быть пустым.")
            return

        while True:
            try:
                price = float(input("Введите цену цветка: "))
                if price < 0:
                    raise ValueError("Цена не может быть отрицательной.")
                break
            except ValueError as e:
                print(f"Ошибка ввода: {e}. Пожалуйста, введите корректную цену.")

        flowers.append(Flower(name, price))
        print(f"Цветок '{name}' добавлен!")

    def remove_flower(self, flowers: list[Flower]):
        name = input("Введите название цветка для удаления: ")
        if not name.strip():
            print("Название цветка не может быть пустым.")
            return
        
        for flower in flowers:
            if flower.name.lower() == name.lower():
                flowers.remove(flower)
                print(f"Цветок '{name}' удален!")
                return
        
        print(f"Цветок '{name}' не найден.")

    def update_flower(self, flowers: list[Flower]):
        name = input("Введите название цветка для обновления: ")
        if not name.strip():
            print("Название цветка не может быть пустым.")
            return

        for flower in flowers:
            if flower.name.lower() == name.lower():
                new_name = input(f"Введите новое название (текущее: {flower.name}): ") or flower.name
                
                while True:
                    try:
                        new_price = float(input(f"Введите новую цену (текущая: {flower.price}): "))
                        if new_price < 0:
                            raise ValueError("Цена не может быть отрицательной.")
                        break
                    except ValueError as e:
                        print(f"Ошибка ввода: {e}. Пожалуйста, введите корректную цену.")
                
                flower.name = new_name
                flower.price = new_price
                
                print(f"Цветок '{name}' успешно обновлен!")
                return
        
        print(f"Цветок '{name}' не найден.")

    def sort_flowers(self, flowers: list[Flower]):
        sort_choice = input("Сортировать по (1 - имени, 2 - цене): ")
        
        if sort_choice == "1":
            sorted_flowers = sorted(flowers, key=lambda x: x.name)
        elif sort_choice == "2":
            sorted_flowers = sorted(flowers, key=lambda x: x.price)
        else:
            print("Неверный выбор сортировки.")
            return
        
        print("\n--- Цветы после сортировки ---")
        for flower in sorted_flowers:
            print(f"{flower.name} - {flower.price} руб.")

    def filter_flowers(self, flowers: list[Flower]):
        try:
            min_price = float(input("Введите минимальную цену: "))
            max_price = float(input("Введите максимальную цену: "))
            
            filtered_flowers = [flower for flower in flowers if min_price <= flower.price <= max_price]
            
            if filtered_flowers:
                print("\n--- Отфильтрованные цветы ---")
                for flower in filtered_flowers:
                    print(f"{flower.name} - {flower.price} руб.")
            else:
                print("Нет цветов в указанном диапазоне цен.")
        except ValueError:
            print("Пожалуйста, введите корректные числовые значения для цен.")

    def view_users(self, users: list[User]):
        print("\n--- Список пользователей ---")
        for user in users:
            if user.role == 'user':
                print(user.username)
