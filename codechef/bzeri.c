#include <stdio.h>
#include <stdlib.h>    /* for calloc() */
#include <strings.h>   /* for bzero() */

/* Find the number of matching substrings in the string s */
void sub(char *s)
{
    size_t s_len = strlen(s);
    short *matches = (short *) calloc(s_len, sizeof(short));
    short *dups = (short *) calloc(s_len, sizeof(short));
    size_t n = s_len * sizeof(short);    /* used by bzero() */
    size_t len, i, j, stop;

    /* Find all substrings of length 1..s_len */
    for (len=1; len<s_len; ++len)
    {
        bzero((void *) matches, n);    /* zero out the number of matches */
        bzero((void *) dups, n);       /* zero out the duplicates */
        stop = s_len - len + 1;
        for (i=0; i<stop; ++i)
        {
            if (dups[i])    /* this is a duplicate (was already counted) */
                continue;
            for (j=i+1; j<stop; ++j)
            {
                if (memcmp(s+i, s+j, len))    /* substring comparison */
                    continue;    /* not a match? continue */
                matches[i]++;
                dups[j] = 1;
            }
            if (matches[i])
                printf("%d: %.*s\n", matches[i]+1, (int) len, s+i);
        }
    }
}

int main()
{
    sub("abcabcabcabc");
    return 0;
}