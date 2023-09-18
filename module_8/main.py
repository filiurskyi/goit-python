from datetime import datetime

workdays = ["Monday", "Tuesday", "Wednesday", "Thutsday", "Friday"]
weekend = ["Saturday", "Sunday"]


def get_birthdays_per_week(users: list) -> dict:
    '''receives list of dictionaries:
    [{"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()}]
    returns:
    {'Monday': ['Bill', 'Jan'], 'Wednesday': ['Kim']}
    '''
    monday = []
    tuesday = []
    wednesday = []
    thursday = []
    friday = []
    result = []
    
    for workday in workdays:

        for user in users:

            name = user["name"]
            birthday = user["birthday"].strftime("%A %d %B").split()
            print(name)
            print(birthday)

            # missed BD on weekend
            if birthday[0] in weekend:
                pass

    # result = {"Monday": monday, "Tuesday": tuesday,
    #           "Wednesday": wednesday, "Thursday": thursday, "Friday": friday}
    return result


# main loop
if __name__ == '__main__':
    print(get_birthdays_per_week(
        [{"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()}]))
