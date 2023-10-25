from adv.calc import Random

def play_lottery():
    while True:
        inp = input("Enter 5 unique lucky numbers between 1 and 90 (no duplicates): ")
        inp = inp.strip().split(",")
        if len(inp) != 5:
            print("Please enter exactly 5 numbers.")
            continue
        try:
            inp = list(map(int, inp))
            if len(set(inp)) == 5:
                rand = Random(5)
                outcome = rand.random_number()
                if set(outcome) == set(inp):
                    print("You won!")
                else:
                    print(f"You lost. Winning numbers are: {outcome}")
                break
            else:
                print("Please enter 5 unique numbers.")
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")


for i in range(3):
    play_lottery()
