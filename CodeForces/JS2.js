var g = readline().split(" ");
var k = readline().split(" ");
var min = 0;
var arr = [];
for (i = 1; i <= Number(g[0]); i++) {
    arr[i] = 0;
}

for (i = 0; i < k.length; i++) {
    arr[k[i]]++;
}

var flag = true;
for (b = 1; b <= arr.length; b++) {
    if (arr[b] == 0) {
        flag = false;
        break;
    }
}

if (flag) {
    min = arr[1];
    for (b = 2; b <= arr.length; b++) {
        if (min > arr[b])
            min = arr[b];
    }
}
print(min);