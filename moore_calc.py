"""
Moore's law is the observation that the number of transistors in an integrated circuit (IC) doubles about every two years.

This program will compute and display a crude estimate of this law and the resulting computing power this represents

One measure of computing power is the number of Floating-Point Operations Per Second (FLOPS) a computer is capable of
preforming. This program assumes that each transistor results in 50 FLOPS.
If a computer had 100 transistors, it would be assumed (for the purpose of this program) to be capable of 5,000 FLOPS (100 * 50)


The program will prompt the user for the starting number of transistors, the starting year, and the total amount of years
the program will calculate. It will then output Moore's law for every 2 years, including the transistor amount and the
FLOPS computing power for that year.
"""


# this function will format flops, ex. an input of 1000 returns 2 kiloFLOP, an input of 1000000 returns 1 megaFLOP
def formatting(original_flops):
    # create a dictionary that holds all the flop names and their sizes in flops
    unit_definition = {
        'FLOPS': 1,
        'kiloFLOPS': 1000,
        'megaFLOPS': 1000000,
        'gigaFLOPS': 1000000000,
        'teraFLOPS': 1000000000000,
        'petaFLOPS': 1000000000000000,
        'exaFLOPS': 1000000000000000000,
        'zettaFLOPS': 1000000000000000000000,
        'yottaFLOPS': 1000000000000000000000000
    }

    # create a float variable called 'formatted' to save the end result
    formatted = 0.0
    # create a str variable called 'unit_name' to save the unit name that we formatted to
    unit_name = ''

    for unit, conversion_rate in unit_definition.items():
        if original_flops >= conversion_rate:
            formatted = round(original_flops / conversion_rate, 2)
            unit_name = unit

    return f'{formatted:.2f} {unit_name}'


# this function will take in a starting year, transistor amount, and the total years and print Moore's Law for these years
def the_moore_the_merrier():
    print('Project One (01) - Part C: The Moore the Merrier')

    # the variable 'transistors' will be used to save the starting number of transistors that we prompt for
    transistors = int(input('Starting Number of transistors: '))

    # the variable 'starting_year' will be used to save the starting year that we prompt for
    starting_year = int(input('Starting Year: '))

    # the variable 'total_years' will be used to save the total number of years that we prompt for
    total_years = int(input('Total Number of Years: '))

    # create a dictionary to store the count of the year and the number of transistors during that year
    transistor_count = {1: transistors}

    # this variable 'flops_coount' will be used to save the current year's flops count
    flops_count = transistors * 50

    print('\nYEAR : TRANSISTORS : FLOPS:')

    print(starting_year, f'{transistors:,}', f'{formatting(flops_count)}', f'{flops_count:,}')

    for count, year in enumerate(range(starting_year + 2, starting_year + total_years + 1, 2)):

        # add the current year's transistor count
        transistor_count[count + 2] = transistor_count[count + 1] * 2

        # update the flops count
        flops_count = transistor_count[count + 2] * 50

        # format the current years flops with the formatting function
        formatted_flops = formatting(flops_count)

        # print the year, transisters, formatted flops, and flops
        print(year, transistor_count[count + 2], formatted_flops, f'{flops_count:,}')


the_moore_the_merrier()