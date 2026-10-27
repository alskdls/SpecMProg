start_number = 1
end_number = 50
current = start_number
found_lucky = False

while current <= end_number:
  if current % 2 != 0:
    current += 1
    continue

  if current % 7 == 0 and current % 3 != 0:
    print(f'Знайдено "щасливе" число: {current}')
    found_lucky = True
    break

  current += 1

if not found_lucky:
  print('No "lucky" number was found in the range.')