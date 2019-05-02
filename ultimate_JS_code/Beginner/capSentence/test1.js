function isBigEnough(element, index, array)
{
    return element <= 40
}

console.log([12, 5, 8, 30, 40].every(isBigEnough))