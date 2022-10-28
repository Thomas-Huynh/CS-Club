
A = int(input("Pick number for A "))
B = int(input("Pick number for B "))
iteration_count = 0
while A != B:
    if abs(B - (A + 1)) < abs(B - (A / 2)):
        A = A + 1
    else:
        if A % 2 == 0:
            A = A / 2
        else:
            A = A + 1
    iteration_count += 1
print(iteration_count)