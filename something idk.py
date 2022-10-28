N = int(input("How many consecutive numbers do you want? "))
iteration = N % 4

if N >= 1 and N <= 10:
    if iteration == 1 or iteration == 3:
        print("Either")
    elif iteration == 2:
        print("Odd")
    elif iteration == 0:
        print("Even")
else:
    print("Value not in between 1 and 10")



