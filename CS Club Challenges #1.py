import math


#Finding missing side length of right triangle using hypotenuse & 1 side

hypotenuse = float(input("Enter hypotenuse: "))
leg_1 = float(input("Enter a triangle leg: "))
leg_2 = math.sqrt(hypotenuse ** 2 - leg_1 ** 2)
print(f'The other leg is: {leg_2:.2f}')



#Finding missing side length using Law of Cosines

side_1 = float(input("Pick a triangle leg: "))
side_2 = float(input("Pick another triangle leg: "))
angle = float(input("Pick an angle in degrees: ")) * math.pi / 180
if angle >= math.pi:
    print("Dude, not cool.")
else:
    missing_side = math.sqrt(side_1 ** 2 + side_2 ** 2 - 2 * side_1 * side_2 * math.cos(angle))
    print(f'The missing side is: {missing_side:.2f}')


#Keeping word order, but reversing spelling
    
x = input("Type in something: ")
x_list = x.split(" ")
for i in range(len(x_list)):
    word = x_list[i]
    print(word[::-1], end = ' ')


#Keeping spelling, but reversing word order
    
x = input("Type in something: ")
x_list = x.split(" ")
for i in range(len(x_list)):
    word = x_list[(len(x_list) - 1) - i]
    print(word, end = ' ')



