let insertion_sort = (array) => {
  for(let i=1; i<array.length; i++) {
    let temp = array[i];
    let position = i-1;
    while (position >= 0) {
      if (array[position] > temp) {
        array[position+1] = array[position];
      } else {
        break;
      }
      position--;
    }
    array[position+1] = temp;
  }
  return array;
}


array_1 = [4, 2, 9, 7, 1, 8, 3];
console.log(insertion_sort(array_1));