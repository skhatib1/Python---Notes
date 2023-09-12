def even_or_odd(number):

    # Verify input is integer
    if (isinstance(number, str) and not number.isnumeric()) or isinstance(number, float):
        print(f'- {number} is not an integer.')
        return None
    else:
        remainder = int(number) % 2
        if remainder == 0:
            print(f'- {number} is even.')
            return 'even'
        else:
            print(f'- {number} is odd.')
            return 'odd'


even_or_odd(10)
even_or_odd(11)
even_or_odd(5.99)
even_or_odd('10')
even_or_odd('11')
even_or_odd('5.99')