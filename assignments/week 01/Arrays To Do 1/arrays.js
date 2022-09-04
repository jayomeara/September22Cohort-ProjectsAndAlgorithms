// Push front
// pushFront([5,7,2,3], 8) => [8,5,7,2,3]
// pushFront([99], 7) => [7,99]

function pushFront(arr, val) {
  for (let i = arr.length; i >= 0; i--) {
    arr[i] = arr[i - 1];
  }
  arr[0] = val;
  return arr;
}
// console.log(pushFront([5,7,2,3], 8))
// console.log(pushFront([99], 7))

// Pop Front:
// popFront([0,5,10,15]) => 0 returned, with [5,10,15] printed in the function
// popFront([4,5,7,9]) => 4 returned, with [5,7,9] printed in the function

function popFront(arr) {
  let firstNum = arr[0];
  for (let i = 0; i < arr.length; i++) {
    arr[i] = arr[i + 1];
  }
  arr.length = arr.length - 1;
  console.log(arr);
  return firstNum;
}
// console.log(popFront([0, 5, 10, 15]))

// InsertAt:

function insertAt(arr,index,val){
    for (let i = arr.length; i >= index; i--){
        arr[i] = arr [i-1]
    }
    arr[index] = val
    return arr
}
console.log(insertAt([100,200,5], 2, 311))
// insertAt([100,200,5], 2, 311) => [100,200,311,5]
// insertAt([9,33,7], 1, 42) => [9,42,33,7]npm -v
