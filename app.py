fast_mode = input("Do you want fast mode to be enabled?(True/False)> ")
if fast_mode == str("True"):
    print("Fast mode enabled; only the first number the programm found will be a divident of the number")
show_not_primes = str(input("Do you want to show all numbers(True/False)> "))
start_from_number = input("From which number to start?(enter an odd number)> ")
if start_from_number == "":
    number = 3
else:
    number = int(start_from_number)
end = input("Up to which number do you want to execute the programm?> ")


def check_if_prime(number):
    not_prime = []
    for i in range(3, int((number + 1)/2), 2):
        if number%i == 0:
            not_prime.append(i)
            if fast_mode == str("True"):
                break
                      
        #hinzufügen dass wenn anzahl dividenten > vorherigen dann die nummer hinzufügen
    
    if len(not_prime) == 0:
        print(f"Prime Number: {number}")
    else:
        if show_not_primes == str("True"):
            print(f"Not a Prime Number: {number}; Devideable {len(not_prime)} numbers by: {not_prime} and 1 and {number}(itself)")


number_most_deviders = [0]
number_deviders = [0]


while number-2 < int(end):
    check_if_prime(number)
    number += 2
    
while True:
    pass