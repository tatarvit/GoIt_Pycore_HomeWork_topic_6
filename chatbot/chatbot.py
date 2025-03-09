# Функція, яка парсить введені дані користувачем на команду та аргументи
def parse_input(user_input):
    parts = user_input.strip().lower().split()
    action = parts[0] if parts else ''
    args = parts[1:]
    return action, args

# Словник для збереження даних від користувача
contacts = {}

# Додавання нових контактів
def add_contact(args):
    if len(args) < 2:
        return "Помилка: Введіть ім'я та номер телефону" 
    name, phone = args[0], args[1]
    contacts[name] = phone
    return f"Контакт {name} з номером {phone} додано"

# Зміна номера телефона
def change_contact(args):
    if len(args) < 2:
        return "Помилка: Введіть ім'я та номер телефону" 
    name, phone = args[0], args[1]
    if name in contacts:
        contacts[name] = phone
        return f"Контакт {name} оновлено з новим номером {phone}"
    else:
        return f"Контакт {name} не знайдено"
    
# Повертає номер телефону для заданого імені
def show_phone(args):
    if len(args) < 1:
        return "Помилка: Введіть ім'я"
    name = args[0]
    return contacts.get(name, f"Контакт {name} не знайдено")

# Показує всі контакти
def show_all():
    if not contacts:
        return ""
    return "\n".join([f"{name}:{phone}" for name, phone in contacts.items()])

# Основний цикл роботи чатбота
def main():
    print("Привіт! Я консольній бот-помічник.")
    while True:
        user_input = input("Введіть данні наступним чином команду(add, change, phone, all) ім'я номер телефону ")
        command, args = parse_input(user_input)
        
        if command in ("exit", "close"):
            print("До побачення!")
            break
        elif command == "add":
            print(add_contact(args))
        elif command == "change":
            print(change_contact(args))
        elif command == "phone":
            print(show_phone(args))
        elif command == "all":
            print(show_all())
        else:
            print("Невідома комфнда. Спробуй ще раз")
            
if __name__ == "__main__":
    main()