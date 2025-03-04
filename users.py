from personality import Personality
from flowers import Flower

class User(Personality):
    def __init__(self, username: str, password: str):
        super().__init__(username, password, role="user")
        self._history = []

    @property
    def history(self):
        return self._history

    def display_info(self):
        print(f"Пользователь: {self.username}, Роль: {self.role}")

    @staticmethod
    def create_user(users: list):
        new_username = input("Введите новый логин: ")
        new_password = input("Введите новый пароль: ")

        if not new_username.strip() or not new_password.strip():
            print("Логин и пароль не могут быть пустыми.")
            return

        for user in users:
            if user.username == new_username and user.role == "user":
                print("Пользователь с таким логином уже существует!")
                return

        new_user = User(new_username, new_password)
        users.append(new_user)
        print(f"Пользователь '{new_username}' успешно создан!")

    @staticmethod
    def view_flowers(flowers: list[Flower]):
        print("\n--- Доступные цветы ---")
        for flower in flowers:
            print(f"{flower.name} - {flower.price} руб.")

    def buy_flower(self, flowers: list[Flower]):
        flower_name = input("Введите название цветка для покупки: ")
        for flower in flowers:
            if flower.name.lower() == flower_name.lower():
                self._history.append(flower_name)
                print(f"Цветок '{flower_name}' успешно куплен!")
                return
        print("Цветок не найден.")

    def view_history(self):
        print("\n--- Ваша история покупок ---")
        if not self._history:
            print("Вы еще ничего не купили.")
        for item in self._history:
            print(item)

    def update_profile(self):
        new_password = input("Введите новый пароль: ")
        if new_password.strip():
            self.password = new_password
            print("Пароль успешно обновлен.")
        else:
            print("Пароль не может быть пустым.")