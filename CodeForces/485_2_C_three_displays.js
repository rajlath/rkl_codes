var n = parseInt(readline())
var map = Array.prototype.map;
var f = Array.prototype.map.call(readline().split(' '), parseInt);
var c = Array.prototype.map.call(readline().split(' '), parseInt);
//var f = readline().split(' ').map(x => Number(x));
//var c = readline().split(' ').map(x => Number(x));

var maxv = Number.MAX_SAFE_INTEGER + 1;

var ans = maxv;

for (var i = 0; i < n; i++) {
    var l = maxv;
    var r = maxv;
    for (var j = i + 1; j < n; j++) {
        if (f[i] < f[j]) r = Math.min(r, c[j]);
    }
    for (var j = n - 1; j > -1; j--) {
        if (f[j] < f[i]) l = Math.min(l, c[j]);
    }
    if (l != maxv && r != maxv) {
        ans = Math.min(ans, l + r + c[i]);
    }
    if (ans == maxv) {
        print(-1);
    } else {
        print(ans);
    }

}