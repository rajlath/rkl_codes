#include <bits/stdc++.h>

using namespace std;

// Complete the averageOfTopEmployees function below.
void averageOfTopEmployees(vector<int> rating) {
    int noe = rating.size();
    if s


}

int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    vector<int> rating(n);

    for (int rating_itr = 0; rating_itr < n; rating_itr++) {
        int rating_item;
        cin >> rating_item;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        rating[rating_itr] = rating_item;
    }

    averageOfTopEmployees(rating);

    return 0;
}