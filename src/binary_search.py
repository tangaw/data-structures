def binary_search(array, value):
  lower_bound = 0
  upper_bound = len(array) - 1

  while lower_bound <= upper_bound:
    index = int((lower_bound + upper_bound) / 2)
    if array[index] == value:
      return index
    elif array[index] > value:
      upper_bound = index - 1
    else:
      lower_bound = index + 1
  
  return "Not found"


array_1 = [4, 17, 38, 66, 91]
search_value = 66
print(binary_search(array_1, search_value))