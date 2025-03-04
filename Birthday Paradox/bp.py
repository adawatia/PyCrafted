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
888888b.   d8b         888    888           888                         8888888b.                                 888                   
888  "88b  Y8P         888    888           888                         888   Y88b                                888                   
888  .88P              888    888           888                         888    888                                888                   
8888888K.  888 888d888 888888 88888b.   .d88888  8888b.  888  888       888   d88P  8888b.  888d888  8888b.   .d88888  .d88b.  888  888 
888  "Y88b 888 888P"   888    888 "88b d88" 888     "88b 888  888       8888888P"      "88b 888P"       "88b d88" 888 d88""88b `Y8bd8P' 
888    888 888 888     888    888  888 888  888 .d888888 888  888       888        .d888888 888     .d888888 888  888 888  888   X88K   
888   d88P 888 888     Y88b.  888  888 Y88b 888 888  888 Y88b 888       888        888  888 888     888  888 Y88b 888 Y88..88P .d8""8b. 
8888888P"  888 888      "Y888 888  888  "Y88888 "Y888888  "Y88888       888        "Y888888 888     "Y888888  "Y88888  "Y88P"  888  888 
                                                              888                                                                       
                                                         Y8b d88P                                                                       
                                                          "Y88P"                                                                          
""")

def main():
    pass

if __name__ == "__main__":
    main()