
using namespace std;
 
int main()
{
    int n;
    cin>>n;
    int *a=new int[n];
    int sum=0;
    int has[n+1];
    has[0]=0;
    for(int i=0;i<n;i++){
        cin>>a[i];
        sum+=a[i];
    }
    int j=0;
    for(int i=0;i<n;i++){
        int tmp=sum-a[i];
        if(i!=0 && i+1!=n){
            if(tmp%3==0 && a[i-1]+a[n-1]==10)
                j++;
        }
        else{
            if(i==0){
                if(tmp%3==0 && a[n-1]==0)
                    j++;
            }
            else{
                if(tmp%3==0 && a[i-1]==0)
                    j++;
            }
        }
        has[i+1]=j;
    }
    
    int q;
    cin>>q;
    while(q--){
        int l,r;
        cin>>l>>r;
        cout<<has[r]-has[l-1]<<endl;
    }
    return 0;
}
