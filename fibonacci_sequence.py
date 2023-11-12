# this function will prompt the user for a number and will print the fibonacci sequence up to that sequence number
def fibonacci_sequence():
    print('Project One (01) - Part A : Fibonacci Sequence')

    # this variable will be used to save the last sequence number the user wants to print
    last_sequence = int(input('Sequence ends at:  '))

    # this dictionary will be used to save each fibonacci number and it's sequence number
    fibonacci = {0: 0, 1: 1}

    print('0: 0 0')
    print('1: 1 1')

    for i in range(2, last_sequence + 1):
        # add an entry to the dictionary with the key as the sequence number (i) and the value as the sum of the previous two numbers
        fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]
        # print the sequence number (i), the current fibonacci number, and the current fibonacci number formatted with commas
        print(f'{i}: {fibonacci[i]} {fibonacci[i]:,}')

    
fibonacci_sequence()