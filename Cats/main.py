import os
from cat_card.get_cats_info import get_info  # Импортируем функцию из get_cats_info.py

if __name__ == '__main__':
    # Отримуємо шлях до поточної папки
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Додаємо до цього шляху ім'я файла
    path = os.path.join(current_dir, 'cat_card', 'info_cats.txt')
    
    # Перевіряємо, чи існує такий файл
    if not os.path.exists(path):
        print(f'Помилка: Файл "{path}" не знайдено. Перевірь коректність шляху до файла')
    else:
        # Отримуємо інформацію про котів
        cat_info = get_info(path)
        
        if cat_info:
            print(f'Інформація про котів:\n{cat_info}')
        else:
            print('Інформація не знайдена або файл порожній.')
