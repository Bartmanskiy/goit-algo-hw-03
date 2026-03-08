import random

def get_numbers_ticket(min, max, quantity):
    new_set = set()
    while len(new_set) < quantity:    
        number = random.randint(min, max) 
        new_set.add(number)
        new_list = sorted(new_set)
    return new_list


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)