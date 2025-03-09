import os

def get_salary(path):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'salary.txt')
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                try:
                    _, salary = line.strip().split(',')
                    salaries.append(int(salary))
                except ValueError:
                    print(f'Помилка обробки рядка: {line.strip()}')
                    
            if not salaries:
                print('Файл не містить коректних даних про зарплату')
                return(0,0)
            
            total_salary = sum(salaries)
            average_salary = total_salary / len(salaries)
            
            return(total_salary, average_salary)
        
    except FileNotFoundError:
        print('Файл не знайдено')
        return (0,0)
    except Exception as unexpected_error:
        print(f'Несподівана помилка: {unexpected_error}')
        return(0,0)   
        
# # Виклик функції
# total_salary, average_salary = get_salary()
# print(f'Загальна сума заробітної плати: {total_salary}, середня заробітна плата: {average_salary}')