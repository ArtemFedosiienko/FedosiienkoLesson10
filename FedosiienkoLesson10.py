#Завдання 1
def get_month(number):
    months = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }
    try:
        return months[number]
    except KeyError as key_error:
        print(key_error, ", use only numbers from 1 to 12")
    except TypeError as type_error:
        print(type_error, ", use only numbers from 1 to 12")

month_name = get_month([1, 2, 3])
print(month_name)


#Завдання 2
def check(sequence):
    if len(set(sequence)) == len(sequence):
        return True
    return False

def check_sequence_unique(array):
    try:
        return check(array)
    except TypeError as type_error:
        print(type_error, 'use only strings, lists or sets')


s = False
u = check_sequence_unique(s)
print(u)

#Завдання 3

class Error(Exception):
    pass

class ValueTooSmallError(Error):
    pass

class ValueTooLargeError(Error):
    pass

number = 10

while True:
    try:
        i_num = int(input("Уведіть число: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("Це число менше загаданого, спробуйте ще раз!\n")
    except ValueTooLargeError:
        print("Це число більше загаданого, спробуйте ще раз!\n")

print("Вітаю! Ви правильно вгадали!")