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


def binary_search_recursive(array, value, lower_bound, upper_bound):
  while lower_bound <= upper_bound:
    index = int((lower_bound + upper_bound) / 2)
    if array[index] == value:
      return index
    elif array[index] > value:
      return binary_search_recursive(array, value, lower_bound, index-1)
    elif array[index] < value:
      return binary_search_recursive(array, value, index+1, upper_bound)
  
  return "Not found"


array_1 = [4, 17, 38, 66, 91]
search_value = 90
print(binary_search(array_1, search_value))
print(binary_search_recursive(array_1, search_value, 0, len(array_1)-1))