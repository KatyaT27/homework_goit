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
        elif today <= birthday <= next_week:
            weekdays_index = (birthday.weekday() - today.weekday()) % 7
            target_day = weekdays[(today.weekday() + weekdays_index) % 7]
            birthdays[target_day].append(user['name'])

    # Виводимо результати
    for day, names in birthdays.items():
        if names:
            print(f"{day}: {', '.join(names)}")
