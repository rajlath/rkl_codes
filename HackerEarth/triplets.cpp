//declare dp array of boolean values of size M
bool dp[M] = {0}; // init with fasle values
for(int i = 0; i < N; i++) {
    bool ndp[M] = {0}; // init temporary boolean array
    ndp[a[i] % M] = 1; // add a subset with one a[i] element
    for(int j = 0; j < M; j++) 
        if(dp[j]) { // if we may find a subset of elements with sum = j (modulo M)
            ndp[j] = 1; // copy existing values
            ndp[(j + a[i]) % M] = 1; // extend the subset with a[i], which will give a sum = j + a[i] (modulo M)
        }
    // copy from ndp to dp before proceeding to the next element of a
    for(int j = 0; j < M; j++) dp[j] = ndp[j];
}

//check dp[0] for the answer
