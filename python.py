users = [
    {
        'username': 'user1',
        'password': 'pass1',
        'role': 'user',
        'history': [],
    },
    {
        'username': 'admin1',
        'password': 'adminpass',
        'role': 'admin',
        'history': [],
    }
]

flowers = [
    {'name': 'Сате сате', 'price': 100},
    {'name': 'Чихпых', 'price': 80},
    {'name': 'Гладиолус', 'price': 120},
    {'name': 'Роза', 'price': 1000}
]


def user_menu(current_user):
    while True:
        print("\n--- Пользовательское меню ---")
        print("1. Просмотреть доступные цветы")
        print("2. Купить цветы")
        print("3. Просмотреть историю покупок")
        print("4. Обновить профиль")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            view_flowers()
        elif choice == "2":
            buy_flower(current_user)
        elif choice == "3":
            view_history(current_user)
        elif choice == "4":
            update_profile(current_user)
        elif choice == "5":
            break
        else:
            print("Неверный выбор, попробуйте снова.")

def view_flowers():
    print("\n--- Доступные цветы ---")
    for flower in flowers:
        print(f"{flower['name']} - {flower['price']} руб.")

def buy_flower(current_user):
    flower_name = input("Введите название цветка для покупки: ")
    for flower in flowers:
        if flower['name'].lower() == flower_name.lower():
            current_user['history'].append(flower_name)
            print(f"Цветок '{flower_name}' успешно куплен!")
            return
    print("Цветок не найден.")

def view_history(current_user):
    print("\n--- Ваша история покупок ---")
    if not current_user['history']:
        print("Вы еще ничего не купили.")
    for item in current_user['history']:
        print(item)

def update_profile(current_user):
    new_password = input("Введите новый пароль: ")
    if new_password.strip():
        current_user['password'] = new_password
        print("Пароль успешно обновлен.")
    else:
        print("Пароль не может быть пустым.")

def admin_menu():
    while True:
        print("\n--- Административное меню ---")
        print("1. Добавить цветок")
        print("2. Удалить цветок")
        print("3. Обновить цветок")  
        print("4. Просмотреть всех пользователей")
        print("5. Создать нового администратора")  
        print("6. Сортировать цветы")
        print("7. Фильтровать цветы по цене")
        print("8. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_flower()
        elif choice == "2":
            remove_flower()
        elif choice == "3":
            update_flower()  
        elif choice == "4":
            view_users()
        elif choice == "5":
            create_admin()  
        elif choice == "6":
            sort_flowers()
        elif choice == "7":
            filter_flowers()
        elif choice == "8":
            break
        else:
            print("Неверный выбор, попробуйте снова.")

def add_flower():
    name = input("Введите название цветка: ")
    
    while True:
        try:
            price = float(input("Введите цену цветка: "))
            if price < 0:
                raise ValueError("Цена не может быть отрицательной.")
            break
        except ValueError as e:
            print(f"Ошибка ввода: {e}. Пожалуйста, введите корректную цену.")
    
    flowers.append({'name': name, 'price': price})
    print(f"Цветок '{name}' добавлен!")

def remove_flower():
    global flowers 
    name = input("Введите название цветка для удаления: ")
    
    for flower in flowers:
        if flower['name'].lower() == name.lower():
            flowers[:] = [f for f in flowers if f['name'].lower() != name.lower()]
            print(f"Цветок '{name}' удален!")
            return
    
    print(f"Цветок '{name}' не найден.")

def update_flower():
    global flowers
    name = input("Введите название цветка для обновления: ")
    
    for flower in flowers:
        if flower['name'].lower() == name.lower():
            new_name = input(f"Введите новое название (текущее: {flower['name']}): ") or flower['name']
            
            while True:
                try:
                    new_price = float(input(f"Введите новую цену (текущая: {flower['price']}): "))
                    if new_price < 0:
                        raise ValueError("Цена не может быть отрицательной.")
                    break
                except ValueError as e:
                    print(f"Ошибка ввода: {e}. Пожалуйста, введите корректную цену.")
            
            flower['name'] = new_name
            flower['price'] = new_price
            
            print(f"Цветок '{name}' успешно обновлен!")
            return
    
    print(f"Цветок '{name}' не найден.")

def sort_flowers():
    sort_choice = input("Сортировать по (1 - имени, 2 - цене): ")
    
    if sort_choice == "1":
        sorted_flowers = sorted(flowers, key=lambda x: x['name'])
    elif sort_choice == "2":
        sorted_flowers = sorted(flowers, key=lambda x: x['price'])
    else:
        print("Неверный выбор сортировки.")
        return
    
    print("\n--- Цветы после сортировки ---")
    for flower in sorted_flowers:
        print(f"{flower['name']} - {flower['price']} руб.")

def filter_flowers():
    min_price = float(input("Введите минимальную цену: "))
    max_price = float(input("Введите максимальную цену: "))
    
    filtered_flowers = list(filter(lambda f: min_price <= f['price'] <= max_price, flowers))
    
    if filtered_flowers:
        print("\n--- Отфильтрованные цветы ---")
        for flower in filtered_flowers:
            print(f"{flower['name']} - {flower['price']} руб.")
    else:
        print("Нет цветов в указанном диапазоне цен.")

def view_users():
    print("\n--- Список пользователей ---")
    for user in users:
        if user['role'] == 'user':
            print(user['username'])

def create_user():
    new_username = input("Введите новый логин: ")

    for user in users:
        if user['username'] == new_username:
            print("Пользователь или администратор с таким логином уже существует!")
            return

    new_password = input("Введите новый пароль: ")
    if not new_username.strip(): 
        print("Логин не может быть пустым.")
        return

    if not new_password.strip():
        print("Пароль не может быть пустым.")
        return

    users.append({
        'username': new_username,
        'password': new_password,
        'role': 'user',
        'history': [],
    })

    print(f"Пользователь '{new_username}' успешно создан!")

def create_admin():
    new_username = input("Введите новый логин администратора: ")

    for user in users:
        if user['username'] == new_username:
            print("Администратор или пользователь с таким логином уже существует!")
            return

    new_password = input("Введите новый пароль администратора: ")
    if not new_username.strip():
        print("Логин не может быть пустым.")
        return

    if not new_password.strip(): 
        print("Пароль не может быть пустым.")
        return

    users.append({
        'username': new_username,
        'password': new_password,
        'role': 'admin',
        'history': [],
    })

    print(f"Администратор '{new_username}' успешно создан!")

def main():
    while True:
        action = input("Хотите создать новый логин и пароль (1) или войти под существующим (2)? Выход из программы(3): ").strip().upper()

        if action == "1":
            role_choice = input("Выберите роль (1 - пользователь, 2 - администратор): ").strip()
            if role_choice == "1":
                create_user()
            elif role_choice == "2":
                create_admin()
            else:
                print("Неверный выбор роли.")
        
        elif action == "2":
            if not users:
                print("Нет зарегистрированных пользователей.")
                continue
            
            username = input("Логин: ")
            password = input("Пароль: ")

            for user in users:
                if user['username'] == username and user['password'] == password:
                    if user['role'] == 'user':
                       user_menu(user) 
                    elif user['role'] == 'admin':
                       admin_menu()
                    break
            else:
                print("Неверный логин или пароль.")
       
        elif action == "3":
            return
        
        else:   
            print("Неверный выбор, попробуйте снова.")

main()