from application.salary import *
from application.db.people import *
from datetime import *

if __name__ == '__main__':
    print(f'Сегодня день: {datetime.today().strftime("%d-%m-%Y")}')
    get_employees()
    calculate_salary()