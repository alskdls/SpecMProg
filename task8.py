raw_cars = "aUdi; bmW; pOrScHe ; toYoTa; MeRcEdEs "

# 1
cars_list = raw_cars.split(";")

# 2
for i in range(len(cars_list)):
  cleaned = cars_list[i].strip().capitalize()
  if cleaned.lower() == "bmw":
    cleaned = "BMW"
  cars_list[i] = cleaned

print("Впорядкований список:", cars_list)

# 3
cars_list = cars_list[1::2]

# 4
cars_string = " // ".join(cars_list)

print("Результат у вигляді стрічки:", cars_string)