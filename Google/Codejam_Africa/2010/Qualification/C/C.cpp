// C.cpp : Defines the entry point for the console application.
//



#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;


void solve()
{
	int N;
	cin >> N;
	for (int t=0;t<N;t++)
	{
		char buf[65536];
		if (t==0)
			cin.getline(buf, 65536);
		cin.getline(buf, 65536);
		string ss = buf;

		cout << "Case #" << (t+1) << ": ";
		char prev = '!';
		for (int i=0;i<ss.length();i++)
		{
			string cmd = "";
			switch (ss[i])
			{
			case 'a': cmd = "2"; break;
			case 'b': cmd = "22"; break;
			case 'c': cmd = "222"; break;
			case 'd': cmd = "3"; break;
			case 'e': cmd = "33"; break;
			case 'f': cmd = "333"; break;
			case 'g': cmd = "4"; break;
			case 'h': cmd = "44"; break;
			case 'i': cmd = "444"; break;
			case 'j': cmd = "5"; break;
			case 'k': cmd = "55"; break;
			case 'l': cmd = "555"; break;
			case 'm': cmd = "6"; break;
			case 'n': cmd = "66"; break;
			case 'o': cmd = "666"; break;
			case 'p': cmd = "7"; break;
			case 'q': cmd = "77"; break;
			case 'r': cmd = "777"; break;
			case 's': cmd = "7777"; break;
			case 't': cmd = "8"; break;
			case 'u': cmd = "88"; break;
			case 'v': cmd = "888"; break;
			case 'w': cmd = "9"; break;
			case 'x': cmd = "99"; break;
			case 'y': cmd = "999"; break;
			case 'z': cmd = "9999"; break;
			case ' ': cmd = "0"; break;
			}
			if (cmd[0]==prev)
			{
				cout << " ";
			}
			cout << cmd;
			prev = cmd[cmd.length()-1];
		}
		cout << endl;
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	solve();
	return 0;
}

