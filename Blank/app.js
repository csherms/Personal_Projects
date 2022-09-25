let myArray = [true, false, true, false, true, false];

function countTrue(arr) {
  let count = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === true) {
      count += 1;
    }
  }
  return count;
}

console.log(countTrue(myArray));
