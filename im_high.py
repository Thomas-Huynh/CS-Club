def highLow (integer):
    holding = integer
    holding_list = []
    low = [1, 2, 3, 4]
    high = [5, 6, 7, 8, 9]
    lohi_list = []
    while holding > 0:
        holding_list.append(holding % 10)
        holding = holding // 10
    for i in range(len(holding_list)):
        if holding_list[i] in low:
            lohi_list.append("low")
        elif holding_list[i] in high:
            lohi_list.append("high")
    while len(lohi_list) > 0:
        if len(lohi_list) == 1:
            return True
            break
        else:
            if lohi_list[len(lohi_list) - 1] == lohi_list[len(lohi_list) - 2]:
                return False
                break
            else:
                lohi_list.pop()


user_input = int(input("Enter a number: "))
print(highLow(user_input))