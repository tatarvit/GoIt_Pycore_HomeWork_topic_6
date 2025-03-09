import os
from Salary import get_salary

if __name__ == '__main__':
    # Отримуємо шлях до поточної папки (де знаходиться main.py)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Додаємо до цього шляху ім'я файла
    path = os.path.join(current_dir, 'Salary', 'salary.txt')

    # Перевірка, існує такий файл
    if not os.path.exists(path):
        print(f"Помилкака: Файл '{path}' не знайдено. Перевірь шлях!")
    else:
        total_salary, average_salary = get_salary(path)
        print(f'Загальна сума заробітної плати: {total_salary}. Cередня заробітна плата: {average_salary}')