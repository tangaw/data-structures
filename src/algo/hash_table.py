import string

def intersection(arr1, arr2):
  hashTable = {}
  cross = []

  for e in arr1:
    hashTable[e] = True
  
  for f in arr2:
    if f in hashTable.keys():
      cross.append(f)
  
  return cross


def duplicate_value(arr):
  hashTable = {}
  repeat = []

  for e in arr:
    if e not in hashTable.keys():
      hashTable[e] = True
    else:
      repeat.append(e)
    
  return repeat


def missing_letter(text):
  deconstructed = list(text)
  existing = {}
  for e in deconstructed:
    existing[e] = True
  
  for a in list(string.ascii_lowercase):
    if a not in existing.keys():
      return a


def first_non_duplicate(text):
  string_arr = list(text)
  counts = {}

  for e in string_arr:
    if e not in counts.keys():
      counts[e] = 1
    else:
      counts[e] += 1
  
  for e in string_arr:
    if counts[e] == 1:
      return e
  
  return "No singled out letters!"
    


if __name__ == "__main__":
  ### Testing for intersection() ###
  # arr1 = [1, 2, 3, 4, 5]
  # arr2 = [2, 4, 6]
  # print(intersection(arr1, arr2))

  ### Testing for duplicate_value() ###
  # letters = ['a', 'b', 'c', 'd', 'b', 'e', 'c', 'f', 'g', 'e']
  # print(duplicate_value(letters))

  ### Testing for missing_letter() ###
  # text = "the quick brown box jumps over a lazy dog"
  # print(missing_letter(text))

  ### Testing for first_non_duplicate ###
  text = 'minimum'
  print(first_non_duplicate(text))