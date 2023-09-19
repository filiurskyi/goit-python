from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    result = {}
    current_date = date.today()
    one_day = timedelta(days=1)
    two_days = timedelta(days=2)
    five_days = timedelta(days=5)
    next_monday_date = current_date
    while next_monday_date.strftime("%A") != "Monday":
        next_monday_date += one_day
    for user in users:
        birthday = user["birthday"]
        name = user["name"]

        year_delta = timedelta(days=365.25)
        if birthday < current_date:
            while birthday.strftime("%Y") != str(current_date.year):
                birthday += year_delta
        else:
            while birthday.strftime("%Y") != str(current_date.year):
                birthday -= year_delta

        day_name = str(birthday.strftime("%A")).strip()

        previous = next_monday_date - two_days
        following = next_monday_date + five_days

        print(f"{previous} < {birthday} < {following}")

        if previous < birthday < following:
            if day_name == "Saturday" or day_name == "Sunday":
                if result.get("Monday", None):
                    result["Monday"].append(name)
                else:
                    result.update({"Monday": name})
            else:
                if result.get(day_name, None):
                    result[day_name].append(name)
                else:
                    result.update({day_name: name})
        else:
            continue
    print(f"FINAL RES IS {result}")
    return result


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
