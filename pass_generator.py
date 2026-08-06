       elif(task ==2):
            print(
                "1. word less than 3 words reversed\n\n 2. atleast or more than three words \n (a)fisrt word at the last and three random modules present at the end ans well as front "
            )
    except:
        print("Enter 1 or 2 as your integer:")

40



if a >= 10:
    raise ValueError("Invalid input \n Enter Your Number Below 10")


b = input("Number b/w 5&9:")
if b == "quit":
    print("Yeahhh")
elif not b.isdigit():
    raise ValueError("Not An Integer")
else:
    b=int(b)
    if (b > 5) and (b < 9):
        print(b)
    else:
        raise ValueError
    38