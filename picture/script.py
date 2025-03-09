import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація бібліотеки colorama
init(autoreset=True)

def output_directory_structure(directory: Path, indent: str = ''):
    """Функція рекурсивно обходить директорію та виводить її структуру з кольорами."""
    try:
        for item in sorted(directory.iterdir()):
            if item.is_dir():
                print(f'{indent}{Fore.BLUE}{item.name}{Style.RESET_ALL}/')
                output_directory_structure(item, indent + '  ')  # Рекурсія для вкладених папок
            else:
                print(f'{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}')
    except PermissionError:
        print(f'{indent}{Fore.RED}Доступ заборонено: {directory}{Style.RESET_ALL}')

def main():
    """Основна функція: перевіряє аргумент, шлях та викликає виведення структури."""
    if len(sys.argv) < 2:
        print(f'{Fore.RED}Помилка: Вкажіть шлях до директорії як аргумент командного рядка!{Style.RESET_ALL}')
        print(f'{Fore.YELLOW}Приклад використання: python script.py "шлях_до_папки"{Style.RESET_ALL}')
        return

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(f'{Fore.RED}Помилка: Вказаний шлях не існує!{Style.RESET_ALL}')
        return

    if not directory_path.is_dir():
        print(f'{Fore.RED}Помилка: Вказаний шлях не є директорією!{Style.RESET_ALL}')
        return

    print(f'{Fore.YELLOW}Структура директорії:{Style.RESET_ALL}')
    
    # Викликаємо функцію, яка виводить структуру директорії
    output_directory_structure(directory_path)

if __name__ == '__main__':
    main()
