from datetime import datetime

# days = ["Monday", "Tuesday", "Wednesday", "Thutsday", "Friday", "Saturday", "Sunday"]

def get_birthdays_per_week(users: list) -> dict:
    '''receives list of dictionaries:
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()}
    returns:
    {'Monday': ['Bill', 'Jan'], 'Wednesday': ['Kim']}
    '''
    monday = []
    tuesday = []
    wednesday = []
    thursday = []
    friday = []
    # saturday = []
    # sunday = []

    result = {"Monday":monday, "Tuesday":tuesday, "Wednesday":wednesday, "Thursday":thursday, "Friday":friday}



    return result


# main loop
if __name__ == '__main__':
    print("Error")