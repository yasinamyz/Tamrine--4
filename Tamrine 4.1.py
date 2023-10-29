import random

adade_delkhah = random.randint(0,500)
n_g = 0

while True:
    adade_to = int(input("Enter your num:"))
    n_g+=1

    if adade_delkhah > adade_to:
                print("adade bozorgtr vared kn:")
    if adade_delkhah < adade_to:
            print("adade kuchktr vared kn:")

    if adade_delkhah == adade_to:
            print("Good luck")
    break

print("tedad hadsha" , n_g)