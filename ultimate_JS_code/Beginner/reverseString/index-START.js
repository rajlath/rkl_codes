/* CHALLENGE
Given a string of text, write an algorithm that returns the text received in a reversed format.
E.g reverseString('algorithms') // should return 'smhtirogla'
*/



function reverseString(text) {
    return text.split("").reverse().join("")
}



function reverseString1(text){
    return [...text].reverse().join("")
}



function reverseString2(text){
    let result = ""
    for (let i = text.length - 1; i >= 0; i--){
        result += text[i]
    }
    return result
}

function reverseString3(text){
    result = ""
    for (let char of text){
        result = char + result
    }
    return result
}

function reverseString4(text) {
    if (text === "") {
        return ""
    } else {
        return reverseString4(text.substr(1)) + text[0]
    }
}

function reverseString5(text){
    return text.split("").reduce((acc, char) => char + acc, '')
}

function reverseString6(text){
    return [...text].reduce((acc, char) => char + acc, '')
}

console.log(reverseString("rajlath"))
console.log(reverseString1("rajlath"))
console.log(reverseString2("rajlath"))
console.log(reverseString3("rajlath"))
console.log(reverseString4("rajlath"))
console.log(reverseString5("rajlath"))
console.log(reverseString6("rajlath"))






module.exports = reverseString