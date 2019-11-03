class Solution:
    def removeSubfolders(self, folder) :
        folder = sorted(folder)
        answer = []
        last  = ''
        for f in folder:
            if len(answer) == 0:
                answer.append(f)
            else:
                last = answer[-1]
                if len(f) > len(last) + 1 and last + "/"  == f[:len(last) + 1]:
                    continue
                else:
                    answer.append(f)
        return answer

print(Solution().removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))


'''
vector<string> removeSubfolders(vector<string>& folder) {
sort(ALL(folder));
vector<string> S;
FORR(f,folder) {
    if(S.empty()) S.push_back(f);
    else {
        string a=S.back();
        if(f.size()>a.size()+1 && a+"/"==f.substr(0,a.size()+1)) continue;
        S.push_back(f);


    }
}
return S;
'''