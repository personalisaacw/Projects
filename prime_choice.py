# this function will print all the prime numbers between prompts
def prime_choice():

    print('Part One - Project B: Prime Choice')

    # prompt the user for the starting number and store it in 'starting_number'
    starting_number = int(input('\nPrime Numbers starting with: '))

    # prompt the user for the ending number and store it in 'ending_number'
    ending_number = int(input('and ending with: '))

    # if the starting number is greater than the ending number, switch the two numbers
    if starting_number > ending_number:
        print(f'\nIncorrect Input: {starting_number} is greater than {ending_number}')
        starting_number, ending_number = ending_number, starting_number
        print('The numbers have been automatically switched.')

    print(f'\nPrime numbers in the range from: {starting_number} and {ending_number} are:')

    for num in range(starting_number, ending_number + 1):
        # we will use a boolean variable 'prime' to keep track of if the current number is prime
        prime = True
        if num == 0:
            prime = False
        if num == 1:
            prime = False
        if num < 0:
            prime = False
        # we will use this inner loop to check if the number in the outer loop has any factors aside from 1 and itself
        for factor in range(2, num):
            # if it has a factor, it is not a prime number, so set prime to False
            if num % factor == 0:
                prime = False
        # if 'prime' is true, then the current number in the forloop must be prime, so print that num is prime
        if prime:
            print(f'{num} is prime')


prime_choice()