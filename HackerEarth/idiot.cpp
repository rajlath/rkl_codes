#copied
int pos[2000],val[2000];
string s;
int main(){
	int n,i;
	cin>>n;
	for(i=1;i<=200;i++){
		pos[i]=i;
		val[i]=i;
	}
	char x,y;
	for(i=1;i<=n;i++){
		cin>>x>>y;
		x=tolower(x);
		y=tolower(y);
		int f=val[int(x)];
		int s=val[int(y)];
		val[int(x)]=s;
		val[int(y)]=f;
	}
	for(i=1;i<=200;i++)
	pos[val[i]]=i;
	while(cin>>s){
		for(i=0;i<s.length();i++){
			x=tolower(s[i]);
			if(pos[int(x)]==int(x))
			cout<<s[i];
			else{
				int z=pos[int(x)];
				x=toupper(char(z));
				if(isupper(s[i]))
				cout<<x;
				else
				cout<<char(z);
			}
		}
		cout<<" ";
	}
	return 0;
}
