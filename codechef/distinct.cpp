#include<bits/stdc++.h>

using namespace std;


int CountUniqueCharacters(char* str){
    int count = 0;

    for (int i = 0; i < strlen(str); i++){
         bool appears = false;
         for (int j = 0; j < i; j++){
              if (str[j] == str[i]){
                  appears = true;
                  break;
              }
         }

         if (!appears){
             count++;
         }
    }

    return count;
}

int main()
{
    char str[1000];
    scanf ("%[^\n]%*c", str);


    int cnt = CountUniqueCharacters(str);
    cout<<cnt;
    if(cnt == 26)
    {
        cout<<"Yes\n";
    }
    else
    {
        cout<<"No\n";
    }
    return 0;

}