"""
Знайти сумму елементів: (x**i+n)/(x-n)    i = 1 до n-ого елементу.
"""
def calculate_24():
    base = get_input("Enter base: ")
    limit = get_input("Enter limit: ")
    result = get_result_24(base, limit)
    print("sum24 = " + str(result))
    return get_repeat("Do you want to repeat Y/N")


def get_repeat(message):
    repeat = input(message)
    if repeat.upper() == 'Y' or repeat.lower() == 'yes' or repeat == '':
        return True
    else:
        print("Goodbye!!!")
        return False


def get_result_24(base, limit):
    value = 0
    for degree in range(1, limit + 1):
        value = value + ((pow(base, degree) + limit) / (base - limit))
    return value


def get_input(msg):
    while True:
        n = input(msg)
        if n == 0 :
            print("")

        try:
            int(n)
            break

        except ValueError:
            continue
    return int(n)

print ("Shevchenko Nikolay Km-92")
if __name__ == "__main__":
    while True:
        if not calculate_24():
            break
