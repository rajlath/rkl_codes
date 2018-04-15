#include "std_lib_facilities.h"

vector<int> counts (vector<string> tmp)
{
    vector<int> results;
    int ulcount; //unique letter count

    for (int i = 0; i < tmp.size(); ++i)
    {
        ulcount = 0;
        string cpy = tmp[i];
        for (int j = 0; j < cpy.size(); j++)
        {
            for (int k = 0; k < cpy.size(); ++k)
            {
                if (cpy[j]==cpy[k+j])  //if letter in position j ever equals k, break and try next letter
                {
                    break;
                }
                else ++ulcount;
            }

        }
        results.push_back(ulcount);
    }
    return results;
}

void show_results(vector<int> res)
{
    for (int i=0; i<res.size(); ++i)
    {
        cout << res[i] << " ";
    }
}


int main()
{

    vector<string> input;
    vector<int> counted;
    vector<int> results;

    while(cin != ";")
    {
        input.push_back(cin);
    }
    counts (input);

    show_results(results);

}