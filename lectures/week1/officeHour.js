// #1 Print 1-255
// will need a console.log
// for loop
// activation
function one() {
    for (let i = 1; i <= 255; i++) {
        console.log("printing function 1: ", i)
    }
}
// one()

// #2 Print Sum 0-255 (print each and also the sum)
// sum = 0
// for loop
// console.log
// activate
function two() {
    let sum = 0
    for (let i = 0; i <= 255; i++) {
        sum += i
        console.log("print current value: ", i, "print current sum: ", sum)
    }
}
// two()

// #3 Find and Print Max
// array of numbers
// for loop with conditionals
// console.log
// activation
// var called max
arrThree = [3, 7, 2, 100, 24, 65, 200, -1, 6]
function three(arr) {
    let max = 0
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > max) {
            max = arr[i]
        }
    }
    console.log(max)
}
three(arrThree)

// #4 Array with Odds and Array with Evens

// #5 Greater than Y

// #6 Max, Min, Avg

// #7 Replace negative numbers with a string

// #8 Replace negative numbers with 0 and print the final array