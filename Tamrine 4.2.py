import random

würfel = random.randint(1,6)

while True:
    op = ("Enter würfel oder fertisch")
    if op == "fertisch":
        break

    if op == "würfel":
        print(würfel)
    if würfel == 6:
        print("wieder würfel:")
        würfel = random.randint(1 , 6)  
else:
    print(würfel)

