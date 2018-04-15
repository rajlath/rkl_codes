#include <bits/stdc++.h>
#include <string>

using namespace std;

void findAndReplaceAll(std::string & data, std::string toSearch, std::string replaceStr)
{
	// Get the first occurrence
	size_t pos = data.find(toSearch);

	// Repeat till end is reached
	while( pos != std::string::npos)
	{
		// Replace this occurrence of Sub String
		data.replace(pos, toSearch.size(), replaceStr);
		// Get the next occurrence from the current position
		pos =data.find(toSearch, pos + toSearch.size());
	}
}


int main()
{
        int n, cnt, ans;
        string pat, targ, s;
        scanf("%d",&n);
        for (int i=0;i<n;i++)
        {
            cin>>pat;
            cin>>targ;
            s = targ;
           while (targ.find(pat) != std::string::npos)
            {
                findAndReplaceAll(targ, pat, "");
            }
            ans = (s.length() - targ.length()) / pat.length();
            cout<<ans<< "\n";
        }


    return (0);
}