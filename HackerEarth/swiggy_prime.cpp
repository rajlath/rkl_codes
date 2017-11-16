#include<bits/stdc++.h>
using namespace std;
int main(){
	string str="";
	cin>>str;
	int n = str.length();
	
	string ans = "";
	for(int i=0; i<n; i++){
		if(str[i] != '2' and str[i] != '3' and str[i] != '5' and str[i] != '7'){
			if(str[i]-'0' > 2){
				if(str[i] > '7')ans += "7";
				else if(str[i] > '5')ans += "5";
				else if(str[i] > '3')ans += "3";
				for(int j=i+1; j<n; j++)ans += "7";
				break;
			}	
			else{
				int j = i-1;
				while(j >= 0 and ans[j] == '2')j--;
				string temp = "";
				for(int k=0; k<j; k++)temp += ans[k];
				if(j != -1){
					if(ans[j] == '7')temp += "5";
					else if(ans[j] == '5')temp += "3";
					else if(ans[j] == '3')temp += "2";
			
					for(int k=j+1; k<n; k++)temp += "7";
				}
				else{
					for(int k=1; k<n; k++)temp += "7";
				}
				ans = "";
				ans = temp;
				break;
			}	
		}
		else
			ans += str[i];
	}
	cout<<ans<<endl;
	return 0;
}
