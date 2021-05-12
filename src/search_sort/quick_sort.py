"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
  if len(array) > 1:
    pivot = len(array) - 1
    index = 0

    while (index < pivot):
      while array[index] >= array[pivot]:
        if index == pivot - 1:
          array[index], array[pivot] = array[pivot], array[index]
          pivot -= 1
          break
        array[index], array[pivot-1], array[pivot] = array[pivot-1], array[pivot], array[index]
        pivot -= 1
      index += 1
        
    return quicksort(array[:(pivot-1)]).append(array[pivot]).append(quicksort(array[(pivot+1):]))
    


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))