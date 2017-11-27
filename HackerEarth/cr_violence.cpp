#copied
Brief Description:

Given an integer (NN), then next line consists of NN space separated natural numbers
between 1 and N inclusive such that the  ith number denotes the the crush of boy i
The next line consists of N space separated natural numbers between
1 and N inclusive such that the ith number denotes the the crush of girl i
print two space separated integers, the answer to doctor's questions:

The first answer is the maximum of beats that boy or a girl receives.
The second answer is the number of pairs of students (boys or girls) who beats each other.

Pre-requisites: Basic Programming Skills, Implementation Skills.

Difficulty Level: Easy.

Hints: Store the crush for every boy and every girl in a suitable data structure
For example: Array.

Detailed Editorial:

This Question depends on your implementation skills and how to store the data given in the question.

Firstly: You should have 2 arrays to store the crush of every boy and every girl.
Secondly: You should loop over boys and girls and check if the crush of the boy
(i), girl
(
k
)
(k)
has another crush different from him:

So if that happens, the boy
(
i
)
(i) will beat the girl
(
k
)
(k) crush, so you should increase the beats that
crush of girl
(
k
)
(k) receives.

Redo the same concept and loop over girls and check their crushes.

Thirdly: loop over boys and girls and check which student (boy or a girl)
who receives the maximum number of beats.

Fourthly: loop over boys and girls and check if boy
(
i
)
(i) has a crush girl
(
k
)
(k) and the girl
(
k
)
(k)
has a crush boy
(
j
)
(j), and the crush of the boy
(
j
)
(j) (the girl
(
g
)
(g)) has a crush boy
(
i
)
(i),
So increase the number of pairs who will beat each other.

Note 1: If you got confused by the last step, just think about it as a cycle.

Note 2: Output the number of
p
a
i
r
s
/
2
pairs/2, because you will add the same pair
2
2 times
or make a boolean array which indicates that boy
(
j
)
(j) has been already in a pair,
so when you come to
(
j
)
(j) index, just continue.

Time Complexity:
O
(
C
o
n
s
t
a
n
t
∗
N
)
O(Constant∗N).

Note:
C
o
n
s
t
a
n
t
Constant = number of loops in the code.

Memory Space Complexity:
O
(
C
o
n
s
t
a
n
t
∗
N
)
O(Constant∗N).

Note:
C
o
n
s
t
a
n
t
Constant = number of arrays in the code.

Solution in C++:

#include <bits/stdc++.h>

using namespace std;

int boys [100000 + 10];
int girls [100000 + 10];

int boy_beated[100000 + 10];
int girl_beated [100000 + 10];


int main()
{
    //ios::sync_with_stdio(false);cin.tie(0);

    int n , t, tem1, tem2, tem3;

    cin >>  t;

    while(t--){

        cin >> n;

        memset(boy_beated, 0 , sizeof boy_beated);          // set arrays to 0 in every test case
        memset(girl_beated, 0 , sizeof girl_beated);

        for(int i = 1; i <= n; i++){

            cin >> tem1;
            boys[i] = tem1;
        }

        for(int i = 1; i <= n; i++){

            cin >> tem1;
            girls[i] = tem1;
        }

        for(int i = 1; i <= n; i++){

            if(girls[ boys[i] ] != i) boy_beated[ girls[ boys[i] ] ]++;         // increase the number of beats that this boy take

            if(boys[ girls[i] ] != i) girl_beated[ boys[ girls[i] ]  ]++;
        }

        int maxi = -1;

        for(int i = 1; i <= n; i++) maxi = max(maxi, max(boy_beated[i], girl_beated[i]));       determine the maximum beats

        int pairs = 0;

        for(int i = 1; i <= n; i++){

            int beated_boy = girls[ boys[i] ];

            if(beated_boy != i && i == girls[ boys[beated_boy] ] ) pairs++;         // pair beats each other

            int beated_girl = boys[ girls[i] ];

            if(beated_girl!= i && i == boys[ girls[beated_girl] ] ) pairs++;
        }

        cout << maxi << " " << pairs / 2 << "\n";
    }

    return 0;
}
