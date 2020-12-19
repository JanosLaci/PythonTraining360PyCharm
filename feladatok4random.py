import random

# A generált szám 18 lesz
random.seed(1)
number_to_guess = random.randint(1, 100)

input_number = int(input("Tipp?"))

while number_to_guess != input_number:
    if number_to_guess > input_number:
        print("A szám nagyobb!")
    else:
        print("A szám kisebb")
    input_number = int(input("Következő tipp?"))

print(f'Gratulálok, a szám valóban a/az {input_number:^8d} volt!')
