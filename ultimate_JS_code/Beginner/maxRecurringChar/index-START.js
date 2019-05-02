/* CHALLENGE
Given a string of text, find and return the most recurring character.
e.g maxRecurringChar('aabacada') // will return 'a'
*/



function maxRecurringChar(text) {
    let charMap = {}
    let maxCharCount = 0
    let currMaxChar  = ''
    let charArray = []
    let valsArray = []

    for(let char of text)
    {
        if(charMap.hasOwnProperty(char))
        {
            charMap[char]++
        }
        else
        {
            charMap[char] = 1
        }
        /*
        if (charMap[char] > maxCharCount)
        {
            maxCharCount = charMap[char]
            maxChar = char
        }
        */
    }

    charArray = Object.keys(charMap)
    valsArray = Object.values(charMap)
    maxCharValue = Math.max(...valsArray)
    return charArray[valsArray.indexOf(maxCharValue)]
    //return maxChar
}

console.log(maxRecurringChar("sisusbsnshsjsmskslstsw"))

module.exports = maxRecurringChar;

