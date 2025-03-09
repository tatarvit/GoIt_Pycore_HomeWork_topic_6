import os

def get_info(path):
    path = os.path.join(os.path.dirname(__file__), 'info_cats.txt')
    cats_list=[]
    try:
        with open (path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(',')
                    if len(parts) == 3:
                        cat_id, name, age = parts
                        cats_list.append({'id':cat_id, 'name':name, 'age':age})
                    else:
                        print(f'Неправильний формат рядка: {line}')
    except FileNotFoundError:
        print(f'Файл {path} не знайдено.')
    except Exception as error:
        print(f'сталася помилка: {error}')
        
    return cats_list
    
    
# Перевірка на виконання
# cat_info = get_info('cat_card/info_cats.txt')
# print (cat_info)
