import datetime, random

def get_birthdays(number_of_birthdays):
    birthdays = []
    for i in range(number_of_birthdays):
        start_of_year = datetime.date(2000,1,1)

        random_number_of_days = datetime.timedelta(random.randint(0,364))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)

    return birthdays

def get_match(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None

    for a, birthday_A in enumerate(birthdays):
        for b, birthday_B in enumerate(birthdays[a+1: ]):
            if birthday_A == birthday_B:
                return birthday_A
    pass

print(""" 
______ _      _   _         _              ______                   _           
| ___ (_)    | | | |       | |             | ___ \                 | |          
| |_/ /_ _ __| |_| |__   __| | __ _ _   _  | |_/ /_ _ _ __ __ _  __| | _____  __
| ___ \ | '__| __| '_ \ / _` |/ _` | | | | |  __/ _` | '__/ _` |/ _` |/ _ \ \/ /
| |_/ / | |  | |_| | | | (_| | (_| | |_| | | | | (_| | | | (_| | (_| | (_) >  < 
\____/|_|_|   \__|_| |_|\__,_|\__,_|\__, | \_|  \__,_|_|  \__,_|\__,_|\___/_/\_\
                                     __/ |                                      
                                    |___/                                       
""")

def main():
    pass

if "__name__" ==