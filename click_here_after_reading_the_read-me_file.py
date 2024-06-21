from time import sleep

print("-------------------")
print("Prime Number Finder")
print("-------------------")
print()
print()




fast_mode = input("Do you want fast mode to be enabled?(True/False)> ")
print()
if fast_mode == str("True"):
    print("Fast mode enabled; only the first number the programm finds will be shown")
    print()
show_not_primes = str(input("Do you want all numbers to be shown; False means it will only show the prime numbers?(True/False)> "))
if show_not_primes == str("False"):
    fast_mode = str("True")
print()
start_from_number = int(input("From which number to start?(enter an odd number)> "))
print()
if start_from_number == "":
    number = 3
else:
    number = int(start_from_number)
end = input("Up to which number do you want to execute the programm?> ")
print()

if int(number) == int(start_from_number):
    while_progress = True
else:
    while_progress = False
    
delay = float(input("How long do you want the delay between each iteration to be?(0=as fast as possible)> "))



def check_if_prime(number):
    not_prime = []
    for i in range(3, int((number + 1)/2), 2):
        if number%i == 0:
            not_prime.append(i)
            #delete the '#' in front of the next lines, if you want to choose to show the steps the computer is taking; good for processing singular numbers
            #if str(while_progress) == str("True"):
            #    print(f"New devider found: {i}")
            if fast_mode == str("True"):
                break

    
    if len(not_prime) == 0:
        return(f"Prime Number: {number}")
    
    else:
        if show_not_primes == str("True"):
            return(f"Not a Prime Number: {number}; Devideable by {len(not_prime)} number/s: {not_prime} and 1 and itself({number})")

print()
if not delay == float(0):
    print(f"With your current set time, the programm wil take "+str(((float(end)-float(number))/float(2))*float(delay))+" seconds to finish!")
    print()
    
while number-2 < int(end):
    if check_if_prime(number) == None:
        pass
    else:
        print(check_if_prime(number))
    number += 2
    if delay > 0:
        sleep(delay)
    
print()
print("Re-open programm to execute it multiple times")
print()
while True:
    pass
