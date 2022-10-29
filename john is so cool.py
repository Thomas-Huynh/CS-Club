num_photos = int(input("How many photographs were taken?"))
time = 0
distance = 0
slopes = []
for i in range (num_photos - 1):
    print(f'{time}, {distance}')
    new_time = int(input())
    new_distance = int(input())
    temp_slope = (new_distance - distance) / (new_time - time)
    slopes.append(temp_slope)
    time = new_time
    distance = new_distance

biggest = slopes[0]
for i in range (1, len(slopes)):
    if slopes[i] > biggest:
        biggest = slopes[i]
print(int(biggest))
