// # 1
// Max, Min, Average
// Given an array, print the max, min and average values for that array.
let arr = [0,1,7,2,3,8,4,5]

var max = arr[0]
var min = arr[0]
var average = 0

var sum = 0

function minMaxAvg(arr) {
    console.log(arr.length)
    for(let i=0; i < arr.length; i++) {
        sum += arr[i]
        if(arr[i] > max) {
            max = arr[i]
        }
        if(arr[i] < min) {
            min = arr[i]
        }
    }
    average = sum / arr.length
    console.log("Average is:", average)
    console.log("Max is:", max)
    console.log("Min is:", min)
    return max
}
console.log(minMaxAvg(arr))

// # 2
// Given an array that could contain indexes of arrays,
// determine the amount of numbers in all indexes. Example:
// lengthNested([4,[],8,[9,6,3],7]) returns 6.
// Do not consider there being a third level of nesting
// (something such as [11,[[6]]]).
let arrOne = [4,[],8,[9,6,3],7]

function lengthNested(arr) {
    let count = 0
    for (let i = 0; i < arr.length; i++) {
        console.log("Logging i", arr[i])
        if (Array.isArray(arr[i])) {
            console.log("Yes", i.length)
        }
    }
}
lengthNested(arrOne)

// # 3 
// Same as above, but do not count empty indexes.
// [6, 4, , 8] should return 3, not 4.