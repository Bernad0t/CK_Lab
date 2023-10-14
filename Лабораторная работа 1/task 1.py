numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
for i in range(0, len(numbers) - 1):
    if numbers[i] == None:
        numbers[i] = 0
        numbers[i] = sum(numbers) / (len(numbers))
        break
print("Измененный список:", numbers)
