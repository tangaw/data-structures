let bubble_sort = (array) => {
  let end = array.length - 1;
  let sorted = false;

  while (sorted === false) {
    sorted = true;
    for (i = 0; i < end; i++) {
      if (array[i] > array[i + 1]) {
        let temp = array[i];
        array[i] = array[i+1];
        array[i+1] = temp;
        sorted = false;
      }
    }
    end -= 1;
  }
  return array;
}



let array_1 = [5, 9, 3, 4, 2, 8, 1];
console.log(bubble_sort(array_1));