// removeBlanks(" Pl ayTha tF u nkyM usi c ") => "PlayThatFunkyMusic"
// removeBlanks("I can not BELIEVE it's not BUTTER") => "IcannotBELIEVEit'snotBUTTER"

function removeBlanks(string) {
    //loop through string and identify spaces
    let newString = " ";
    for (let i = 0; i < string.length; i++) {
        if (string[i] != " ") {
        newString += string[i];
        }
    }
    return newString;
    }
console.log(removeBlanks(" Pl ayTha tF u nkyM usi c "));

// getDigits("abc8c0d1ngd0j0!8") => 801008
// getDigits("0s1a3y5w7h9a2t4?6!8?0") => 1357924680

function getDigits(str){
    let newString = " ";
    for(let char in str){
        if(!isNaN(str[char])){
        newString += str[char]
        }
    }
    return Number(newString)
}
console.log(getDigits("abc8c0d1ngd0j0!8"))

// acronym(" there's no free lunch - gotta pay yer way. ") => "TNFL-GPYW".
// acronym("Live from New York, it's Saturday Night!") => "LFNYISN".

function acronym(str) {
    let wordArr = str.split(' ')
    let acronymStr = ' '

    for(let word in wordArr){
        if(wordArr[word].length > 0){
            acronymStr += wordArr[word][0].toUpperCase()
        }
        wordArr[word[0]]
    }
    return acronymStr
}
console.log(acronym(" there's no free lunch - gotta pay yer way. "))

// countNonSpaces("Honey pie, you are driving me crazy") => 29
// countNonSpaces("Hello world !") => 11

function countNonSpaces(str) {
    let counter = 0

    for(let char in str) {
        if(str[char] != ' '){
        counter ++
        }
    }
    return counter
}
console.log(countNonSpaces("Honey pie, you are driving me crazy"))

// removeShorterStrings(['Good morning', 'sunshine', 'the', 'Earth', 'says', 'hello'], 4) => ['Good morning', 'sunshine', 'Earth', 'says', 'hello']
// removeShorterStrings(['There', 'is', 'a', 'bug', 'in', 'the', 'system'], 3) => ['There', 'bug', 'the', 'system']
function removeShorterStrings(arr, len) {
    let shortString = []
    let nextIndex = 0
    for(let value in arr) {
        if(arr[value].length >= len){
            shortString [nextIndex++] = arr[value]
        }
    }
    return shortString
}
console.log(removeShorterStrings(['Good morning', 'sunshine', 'the', 'Earth', 'says', 'hello'], 4))