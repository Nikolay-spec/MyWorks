def engine_of_multiplying():
    for index1 in range(len(a)):
        for index2 in range(len(checking_line)):
            if a[index1] == checking_line[index2]:
                a[index1] *= times_of_multiplying


print("Km-92 Shevchenko Nikolay. ex#24")
flag = ""
while flag == "":
    n = 0
    amount_for_comparing = int(input('How many lines you want to compare:'))
    # amount_for_checking = int(input('Amount of lines to be checked:'))
    times_of_multiplying = int(input('In what times you want to multiply letters:'))
    checking_line = list(input('print checking line:'))
    while n < amount_for_comparing:
        a = list(input('print comparing line:'))
        engine_of_multiplying()
        print('result:', ''.join(a))
        n += 1
        print(
            '---------------------------------------------------------------------------------------------------------')
    flag = input(" if you want to continue : put ENTER , if not : write SOMETHING + ENTER ")
