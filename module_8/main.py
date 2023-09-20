from datetime import date, datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):
    today_date = date.today()
    current_year = today_date.year
    users_list = defaultdict(list)

    if not users:
        return {}

    for user in users:
        name = user['name']
        birthday = user['birthday']
        birthday_this_year = birthday.replace(year=current_year)
        if birthday.month == 1:
            birthday_this_year = birthday.replace(year=current_year + 1)
        else:
            birthday_this_year = birthday.replace(year=current_year)
        if birthday_this_year < today_date:
            continue

        if birthday_this_year.weekday() >= 5:
            birthday_this_year += timedelta(days=(7 -
                                            birthday_this_year.weekday()))

        day_name = birthday_this_year.strftime('%A')
        users_list[day_name].append(name)

    return users_list


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
