from abc import ABC, abstractmethod

class Personality(ABC):
    def __init__(self, username: str, password: str, role: str):
        self._username = username
        self._password = password
        self._role = role

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def role(self):
        return self._role

    @username.setter
    def username(self, value: str):
        if not value.strip():
            raise ValueError("Логин не может быть пустым.")
        self._username = value

    @password.setter
    def password(self, value: str):
        if not value.strip():
            raise ValueError("Пароль не может быть пустым.")
        self._password = value
    
    @abstractmethod
    def display_info(self):
        "Абстрактное свойство для отображения роли."
        pass