




#include <bits/stdc++.h>
using namespace std;
struct node{
	bool isleaf;
	node *next[10];
	node(){
		isleaf =true;
		for(int i=0;i<10;i++){
			next[i] = NULL;

		}
	}
}*root;

void add(string name){
	node *current = root;
	for(int i=0;i<name.size();i++){
		char ch = name[i];

		if(current->next[(int)ch-'a']==NULL){

			current->next[(int)ch-'a'] = new node();
		}
		current->isleaf=false;;
		current = current->next[(int)ch-'a'];

	}
	current->isleaf=true;

}
bool isprefix(string word){
	node *current = root;
	for(int i=0;i<word.size();i++){
		char ch = word[i];

		//if(current->next[(int)ch-'a'])
		current = current->next[(int)ch-'a'];
		if(!current)
			return false;
		if(current && current->isleaf)
			return true;
	}
	if(!current->isleaf)
		return true;
	return false;
}

string str;
int main(void){
	root = new node();
	int n;
	scanf("%d",&n);
	while(n--){
		cin>>str;
		if(isprefix(str)){
			cout << "BAD SET" << endl << str ;
			return 0 ;
		}
		add(str);
	}
	cout << "GOOD SET";
	return 0;

	return 0;
}