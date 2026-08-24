# rock paper scissor:
import random
try:
    while True:
        user_inp = input(
            "Enter \n1 for Rock \t\n2 for scissor\t\n3 for paper\t\n4 for Exiting\t\nEnter Your Choice>>>>>>>>>\n"
        )
        if user_inp.isdigit():
            b = int(user_inp)
            if b == 1 or b == 2 or b == 3:
                r = random.randint(1, 3)
 
