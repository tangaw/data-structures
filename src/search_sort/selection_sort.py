def selection_sort(lst):
  for i in range(len(lst)-1):
    smallestIndex = i
    for j in range(i+1, len(lst)):
      if lst[j] < lst[smallestIndex]:
        smallestIndex = j
    
    if smallestIndex != i:
      lst[i], lst[smallestIndex] = lst[smallestIndex], lst[i]

  return lst



list_1 = [4, 7, 1, 9, 2]
print(selection_sort(list_1))