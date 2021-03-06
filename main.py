import random

def random_number_list(list_size):
    return random.choices(
            range(-1000, 1001),
            k=list_size
        ) # choose 'list_size' element at random from -1000 to 1000 (inclusive)

def run(list_of_number):
    for number in list_of_number:
        if number % 15 == 0: # if the number is divisible by 15, print Gestform and move on to the next number
            print('Gestform')
            continue
        if number % 3 == 0: # if the number is divisible by 3, print Gest and move on to the next number
            print('Gest')
            continue
        if number % 5 == 0: # if the number is divisible by 5, print Form and move on to the next number
            print('Form')
            continue
        print(number) # if none of the previous condition were True, we reach this point, and print the number



if __name__ == "__main__":
    numbers_to_print = random_number_list(20) # a list of 20 randoms element between -1000 and 1000
    # you can simply replace it by any given list of integers for more practical tests
    run(numbers_to_print)
