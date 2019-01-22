class Solution {
    public int subarraysDivByK(int[] A, int K) {
        int [] storedArray = new int[K];
        int sum=0, res=0;
        for(int i=0; i<A.length; i++){
            sum = (((sum + A[i]) % K) + K) % K;
            res += storedArray[sum];
            storedArray[sum]++;
        }
        res += storedArray[0];
        return res;
    }


}