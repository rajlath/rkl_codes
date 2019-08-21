class Solution {
public:
    int minSwaps(vector<int>& data)
    {
        int n, no1=0;
        for(int i=0; i<n ;i++)
        {
	        if(data[i]==1)
	        no1++;
	      }
	      if(no1==0)
        {
	        cout<<"-1\n";
	      }
	      else
        {
	        int curr=0;
	        for(int i=0;i<no1; i++)
	        {
	            if(data[i]==1)
	            curr++;
	        }
	        int mx=curr;

	        for(int i=no1;i<n;i++)
	        {
	            if(data[i]==1)
              {
	                curr++;
	            }
	            if(data[i-no1]==1){
	            curr--;
	           }
	           if(curr>mx){
	            mx=curr;
	           }

	        }
          return no1-mx;
        }
    }
