
#include<bits/stdc++.h>
using namespace std;


int getMax(int arr[], int n)
{
   int result = arr[0];
   for (int i=1; i<n; i++)
      if (arr[i] > result)
         result = arr[i];
    return result;
}


bool isPossible(int time, int K, int job[], int n)
{

    int cnt = 1;

    int curr_time = 0;

    for (int i = 0; i < n;)
    {

        if (curr_time + job[i] > time) {
            curr_time = 0;
            cnt++;
        }
        else {
            curr_time += job[i];
            i++;
        }
    }


    return (cnt <= K);
}


int findMinTime(int K, int T, int job[], int n)
{

    int end = 0, start = 0;
    for (int i = 0; i < n; ++i)
        end += job[i];

    int ans = end;


    int job_max = getMax(job, n);


    while (start <= end)
    {
        int mid = (start + end) / 2;


        if (mid >= job_max && isPossible(mid, K, job, n))
        {
            ans = min(ans, mid);
            end = mid - 1;
        }
        else
            start = mid + 1;
    }

    return (ans);
}

// Driver program
int main()
{
    int job[] =  {10, 7, 8, 12, 6, 8};
    int n = sizeof(job)/sizeof(job[0]);
    int k = 4, T = 5;
    cout << findMinTime(k, T, job, n) << endl;
    return 0;
}
