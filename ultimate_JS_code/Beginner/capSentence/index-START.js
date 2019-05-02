/* CHALLENGE
Given a sentence containing two or more words,
return the equivalent of the sentence when capitalised. E.g
  capSentence('the tales of scotch!') // would return 'The Tales Of Scotch!'
*/




function capSentence1(text) {
   word2Array = text.toLowerCase().split(" ")
   capsArray  = []
   word2Array.forEach( words => {
     capsArray.push(words[0].toUpperCase() + words.slice(1))
   })
   return capsArray.join(" ")
}

function capSentence2(text) {
  let wordsArray = text.toLowerCase().split(' ')
  let capsArray = wordsArray.map(word=>{ return word[0].toUpperCase() + word.slice(1) })

  return capsArray.join(' ')
}

function capSentence(text) {
  let wordsArray = text.toLowerCase().split(' ')
  let capsArray = wordsArray.map( word=>{  return  word.replace(word[0], word[0].toUpperCase()) })
  return capsArray.join(' ')
}


module.exports = capSentence