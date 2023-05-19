from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    # Визначаємо поточну дату та дату через тиждень
    today = datetime.now().date()
    next_week = today + timedelta(days=7)

    # Створюємо словник для днів тижня
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    birthdays = {day: [] for day in weekdays}

    # Перебираємо список користувачів
    for user in users:
        # Отримуємо день народження користувача і виправляємо рік, якщо потрібно
        birthday = user['birthday'].replace(year=today.year if user['birthday'].month > today.month
                                            or (user['birthday'].month == today.month and user['birthday'].day >= today.day)
                                            else today.year + 1)

        # Якщо день народження на вихідних, то привітати в понеділок
        if birthday.weekday() > 4:
            birthdays['Monday'].append(user['name'])
        elif today <= birthday.date() <= next_week:
            weekdays_index = (birthday.date().weekday() - today.weekday()) % 7
            target_day = weekdays[(today.weekday() + weekdays_index) % 7]
            birthdays[target_day].append(user['name'])

    # Повертаємо результати замість їх виводу
    return birthdays


# Перевірка
users = [
    {'name': 'Bill', 'birthday': datetime(1992,5, 18)}, 
    {'name': 'Jill', 'birthday': datetime(1992, 5, 18)},  
    {'name': 'Kim', 'birthday': datetime(1993, 5, 26)},
    {'name': 'Jan', 'birthday': datetime(1993, 5, 26)},
 
]

birthdays_per_week = get_birthdays_per_week(users)



    # Виведення результатів
for day, names in birthdays_per_week.items():
    if names:
        print(f"{day}: {', '.join(names)}")
