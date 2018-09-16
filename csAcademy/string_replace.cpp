'''
Double Replace
Time limit: 1000 ms
Memory limit: 128 MB

You are given 33 strings SS, AA and BB. Replace every substring of SS equal to AA with BB, and every substring equal to BB with AA.

It is possible that two or more substrings matching AA or BB overlap. To avoid confusion about this situation, you should find the leftmost substring that matches AA or BB, replace it, and then continue with the rest of the string.

For example, if S = aabS=aab, A = aaA=aa and B=bbB=bb, we first find the prefix aaaa and replace it with bbbb. Then we continue with the rest of the string that consists only of the last character bb and we stop because we can't find any more matches.

Standard input
The first line contains string SS.

The second line contains string AA.

The third line contains string BB.

Standard output
Print the resulting SS on the first line.

Constraints and notes
The length of all three strings is between 11 and 10001000
A \neq BA≠B
AA and BB will have the same length
Input	Output	Explanation
aab
aa
bb
bbb
We match the first two characters with AA and replacing it with BB we get bbbbbb. Then we continue the algorithm starting at index 33 and we don't find any more matches.

aabbaabb
aa
bb
bbaabbaa
String SS is the concatenation ABABABAB, so in the end we get the concatenation BABABABA
cdabcadb
a
b
cdbacbda
Each character aa gets replaced by bb, and each bb by aa
'''
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;


int main() {
    string s, a, b; cin >> s >> a >> b;
    int l = (int)a.size();
    for (int i = 0; i + l <= (int)s.size(); i += 1) {
        if (s.substr(i, l) == a) {
            s = s.substr(0, i) + b + s.substr(i + l, s.size());
            i += l - 1;
        } else if (s.substr(i, l) == b) {
            s = s.substr(0, i) + a + s.substr(i + l, s.size());
            i += l - 1;
        }
    }
    cout << s << '\n';
    return 0;
}







