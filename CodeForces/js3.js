function main() {
    var x = readline().split(' ').map(Number);
    var a = x[0];
    var b = x[1];
    var seats = readline().split('');

    var aRem = a;
    var bRem = b;

    for (var i = 0; i < seats.length; i++) {
        if (aRem === 0 && bRem === 0) break;
        if (seats[i] === '*') continue;

        if (aRem >= bRem) {
            if (i === 0 || seats[i - 1] !== 'a') {
                aRem--;
                seats[i] = 'a';
            } else if (bRem > 0 && (i === 0 || seats[i - 1] !== 'b')) {
                bRem--;
                seats[i] = 'b';
            }
        } else {
            if (i === 0 || seats[i - 1] !== 'b') {
                bRem--;
                seats[i] = 'b';
            } else if (aRem > 0 && (i === 0 || seats[i - 1] !== 'a')) {
                aRem--;
                seats[i] = 'a';
            }
        }
    }

    print(a + b - aRem - bRem);
}

main();