var g = readline().split(" ");
var y = readline().split(" ");

var k = Number(g[1]);

var out = [];
for (var i = 0; i < y.length; i++) {
    if (y.indexOf(y[i]) === i) {
        out.push(i + 1);
    }
}

if (out.length >= k) {
    print("YES");
    print(out.slice(0, k).join(" "));
} else
    print("NO");