var_start = 10
var_end = 20
found = False

for num in range(var_start, var_end + 1):
  if num % 7 == 0:
    print(f"Знайдено перше число, що ділиться на 7: {num}")
    found = True
    break

if not found:
  print("У заданому діапазоні немає жодного числа, що ділиться на 7.")