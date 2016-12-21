def collatz(number):
    if (number % 2) == 0:
        print( str( number // 2))
        return number // 2
    else:
        print( str( 3 * number + 1))
        return 3 * number + 1

while True:
    try:
        print('Enter number')
        num = int(input())
        break
    except ValueError:
        print("That isn't a number!")

while num != 1:
    num = collatz(num)


