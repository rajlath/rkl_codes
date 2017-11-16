#include <iostream>
#include <stdio.h>
using namespace std;
 
int main()
{
	long r = 0, a[26 + 7] = { 0 };
	char s[2000+7];
	int n;
	scanf("%d", &n);
    scanf("%s",&s);
    for (int i = 0; i < n - 2; i++)
	{
		for (int j = i + 2; j < n; j++)
			if (s[i] == s[j])
				for (int k = i + 1; k<j; k++)
					r += a[s[k] - 'a'];
		a[s[i] - 'a']++;
	}
	printf("%ld\n", r);
	return 0;
}
