# get m from input
def get_number():
    number_of_m = int(input('enter the m:'))
    return number_of_m


# calculate E=mc**2
def calc_to_ein():
    m = get_number()
    c = 300000000
    return m * c ** 2


print(calc_to_ein())
