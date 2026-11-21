numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

numbers.append(60)
print("After append(60):", numbers)

numbers.extend([70, 80])
print("After extend([70, 80]):", numbers)

numbers.insert(2, 25)
print("After insert(2, 25):", numbers)

numbers.remove(25)
print("After remove(25):", numbers)

removed_element = numbers.pop()
print("After pop():", numbers)
print("Removed Element:", removed_element)

numbers.pop(1)
print("After pop(1):", numbers)

print("Index of 40:", numbers.index(40))

numbers.append(40)
print("Count of 40:", numbers.count(40))

numbers.sort()
print("After sort():", numbers)

numbers.sort(reverse=True)
print("After sort(reverse=True):", numbers)

numbers.reverse()
print("After reverse():", numbers)

copied_numbers = numbers.copy()
print("Copied List:", copied_numbers)

numbers.clear()
print("After clear():", numbers)