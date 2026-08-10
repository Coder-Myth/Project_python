 
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
