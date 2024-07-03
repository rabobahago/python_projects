function bubbleSort(arr) {
  let len = arr.length - 1;
  for (let i = 0; i < len; i += 1) {
    let noSwap = true;
    for (let j = 0; j < len - i; j += 1) {
      if (arr[j] > arr[j + 1]) {
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
        noSwap = false;
      }
    }
    if (noSwap) {
      return arr;
    }
  }
  return arr;
}

console.log(bubbleSort([56, 34, 1, 78, 3]));
