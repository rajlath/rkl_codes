/* CHALLENGE
Given a string of text, return the number of vowels found within the text
e.g vowelsCounter('anehizxcv') // will return 3
*/


function vowelsCounter1(text) {
    let counter = 0
    let vowels  =["a", "e", "o", "i", "u"]
    for(let i  of text)
    {
        counter +=  vowels.includes(i)
    }
    return counter
}

function vowelsCounter(text) {
    let count = 0
    let matches = text.match(/[aeiou]/gi);
    if (matches){
       count = matches.length
    }
    return count
}

console.log(vowelsCounter("rajkumarlath"))
console.log(vowelsCounter1("rajkumarlath"))

module.exports = vowelsCounter;
