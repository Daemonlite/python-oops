from adv.calc import Random

rand = Random(5)

inp = input("enter 5 lucky numbers between 1 and 90 : ")

inp.split(",")

outcome = rand.random_number()

if all(inp) in outcome:
    print("you won")
else:
    print(f"You lost, winning numbers are : {outcome}")

